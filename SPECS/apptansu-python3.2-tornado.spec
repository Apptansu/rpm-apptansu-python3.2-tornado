Summary: tornado for apptansu-python3.2
Name: apptansu-python3.2-tornado
Version: 2.2
Release: 1+patched%{?dist}
License: MIT
Vendor: Apptansu
Group: Development/Languages
Source: tornado-%{version}.tgz

BuildRequires: apptansu-python3.2
BuildRequires: apptansu-python3.2-distribute
AutoReq: no
AutoProv: no
Requires: apptansu-python3.2

%define _prefix /usr/lib/apptansu

%description
tornado for apptansu-python3.2

%prep
%setup -q -n tornado-%{version}

%build

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_prefix}/*

%changelog
* Sun Feb 05 2012 Apptansu <support@apptansu.com> 0.2.2-1+patched
- Initial packaging.
