%bcond_without check

Name:           way-edges
Version:        0.12.0
Release:        %autorelease
Summary:        Light weight wayland client focusing on widgets hidden in your screen edge.

License:        MIT
URL:            https://github.com/way-edges/way-edges
Source:         https://github.com/way-edges/way-edges/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  gcc libxkbcommon-devel cairo-devel

%description
Light weight wayland client focusing on widgets hidden in your screen edge.

%prep
%autosetup -n %{name}-%{version} -p1
cargo vendor
# %cargo_prep -v vendor

%build
cargo build --release
# %cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/way-edges

%changelog
%autochangelog
