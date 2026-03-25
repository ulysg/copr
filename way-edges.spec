%bcond_without check

Name:           way-edges
Version:        0.12.1
Release:        %autorelease
Summary:        Light weight wayland client focusing on widgets hidden in your screen edge.

License:        MIT
URL:            https://github.com/way-edges/way-edges
Source:         https://github.com/way-edges/way-edges/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  gcc libxkbcommon-devel cairo-devel pulseaudio-libs

%description
Light weight wayland client focusing on widgets hidden in your screen edge.

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version} -p1
cargo vendor

%build
RUSTFLAGS="--cfg tokio_unstable --cfg tokio_uring" cargo build --release

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp target/release/way-edges $RPM_BUILD_ROOT%{_bindir}

%files
%doc README.md
%{_bindir}/way-edges

%changelog
%autochangelog
