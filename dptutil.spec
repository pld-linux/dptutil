%define	_orgname	raidmgt
Summary:	DPT/Adaptec Storage Management software
Name:		dptutil
Version:	3.31
Release:	1
License:	BSD
Group:		Base
Source0:	http://www.interlude.eu.org/~ad/raidmgt/raidmgt-3.31.tar.gz
# Source0-md5:	a7d0df0ff350ea5ad080e9bd8a3798a3
URL:		http://opensource.adaptec.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
DPT/Adaptec Storage Management software.

%prep
%setup -q -n %{_orgname}-%{version}

%build
for pkg in dptutil dpteng; do
%{__make} -C $pkg clean depend
%{__make} -C $pkg \
	C="%{__cxx}" \
	CC="%{__cxx}" \
	LINK="%{__cxx} %{rpmldflags}" \
	CPP="%{__cxx}" \
	I="-I. %{rpmcflags}" \
	INCLUDE_DIR="-I. %{rpmcflags}"
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install dptutil/raidutil $RPM_BUILD_ROOT%{_sbindir}/dptutil
install dpteng/dpteng $RPM_BUILD_ROOT%{_sbindir}/dpteng

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
