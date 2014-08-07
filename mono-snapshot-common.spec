Summary:	Common helper tools for Mono snapshot packages
Name:		mono-snapshot-common
Version:	00000010
Release:	0
License:	WTFPL
Group:		Development/Languages/Mono
Source:		mono-snapshot
BuildArch:	noarch
URL:		http://www.mono-project.com
%define debug_package %{nil}
%description
This package helps users to manage their environment when using
daily build snapshots of Mono direct from the mono-project.com
site.

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin
cp %SOURCE0 %{buildroot}/usr/bin

%clean
rm -fr %buildroot

%files
%_usr/bin/mono-snapshot
