Name:           student-restrict-ostree
Version:        1.0
Release:        1%{?dist}
Summary:        Restrict netbird, podman usage for student user.

License:        MIT
Requires:       netbird
Requires:	podman
Requires:       acl

BuildArch:      noarch

%description
Applies ACL restrictions to /usr/bin/netbird and /usr/bin/podman to deny execution
for the student user.

%prep
# nothing

%build
# nothing

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
echo "netbird & podman ACL policy package" > %{buildroot}%{_datadir}/%{name}/README

%post
# Apply ACL restriction
if [ -x /usr/bin/netbird ]; then
    /usr/bin/setfacl -m u:student:--- /usr/bin/netbird || :
fi
if [ -x /usr/bin/podman ]; then
    /usr/bin/setfacl -m u:student:--- /usr/bin/podman || :
fi


%postun
# Optional: remove ACL on uninstall
if [ "$1" -eq 0 ] && [ -x /usr/bin/netbird ]; then
    /usr/bin/setfacl -x u:student /usr/bin/netbird || :
fi
if [ "$1" -eq 0 ] && [ -x /usr/bin/podman ]; then
    /usr/bin/setfacl -x u:student /usr/bin/podman || :
fi

%files
%{_datadir}/%{name}/README

%changelog
* Tue Jan 28 2026 Paul Schuldesz <paul.schuldesz@student.upt.ro> - 2.0-1
- Initial package
- Add podman to restriction
