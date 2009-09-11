%define name gsynaptics
%define version 0.9.14
%define release %mkrel 7

Summary: Tool for Synaptics touchpad driver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://globalbase.dl.sourceforge.jp/gsynaptics/28322/%{name}-%{version}.tar.gz
# non-corrupted icon from CVS
Source1: http://cvs.sourceforge.jp/cgi-bin/viewcvs.cgi/*checkout*/gsynaptics/gsynaptics/data/touchpad.png
Patch0: gsynaptics-0.9.14-do-not-set-zero.patch
Patch1: gsynaptics-0.9.14-dot-fixes.patch
Patch2: gsynaptics-0.9.14-fix-desktop-file.patch
Patch3: gsynaptics-0.9.14-fix-docbook.patch
Patch4: gsynaptics-0.9.14-build-filename.patch
Patch5: gsynaptics-0.9.14-format-security.patch

# (cg) Some patches from fedora
Patch100: gsynaptics-0.9.14-fix-tap-statecheck.patch
Patch101: gsynaptics-0.9.14-enable-tapping.patch
Patch102: gsynaptics-0.9.14-dont-reset-taptime.patch


License: GPLv2+
Group: System/Configuration/Hardware
Url: http://gsynaptics.sourceforge.jp/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gnomeui2-devel gnome-doc-utils libglade2-devel

%description
GSynaptics is a setting tool for Synaptics touchpad driver.

%prep
%setup -q
cp -f %{SOURCE1} data
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README TODO
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/autostart/%{name}-init.desktop
%doc %{_datadir}/gnome/help/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_datadir}/pixmaps/touchpad.png
