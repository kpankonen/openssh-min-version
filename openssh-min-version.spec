%define minversionmajor 5.3p1
%define minversionminor 81

Name: openssh-min-version
Version: %{minversionmajor}
Release: %{minversionminor}
Summary: ensures a minimum version of openssh
BuildArch: noarch

Group: Applications/System
License: BSD
URL: https://github.com/kpankonen/openssh-min-version

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides: openssh-min-version = %{version}-%{release}
Requires: openssh >= %{minversionmajor}-%{minversionminor}

%description
Ensures that a minimum version of OpenSSH is installed.

%clean
rm -rf %{buildroot}

%files

%changelog
* Thu Apr 11 2013 kevin.pankonen - 5.3p1-84
- Initial build ensures >= 5.3p1-84
