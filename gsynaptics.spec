%define name gsynaptics
%define version 0.9.14
%define release 7

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
BuildRequires: pkgconfig(libgnomeui-2.0) pkgconfig(gnome-doc-utils) pkgconfig(libglade-2.0)
buildrequires: perl(XML::Parser)

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
%makeinstall_std
%find_lang %{name}

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


%changelog
* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.9.14-7mdv2011.0
+ Revision: 437821
- rebuild

* Thu Apr 23 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.14-6mdv2009.1
+ Revision: 368831
- Drop SHM patch. Using device properties should now work with newer synaptics.

* Sat Apr 18 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.14-5mdv2009.1
+ Revision: 367980
- Update to work with new synaptics driver by using synclient -s

* Fri Mar 06 2009 Colin Guthrie <cguthrie@mandriva.org> 0.9.14-4mdv2009.1
+ Revision: 349615
- Add patches from Fedora
- Fix format security issues

* Thu Oct 16 2008 Frederik Himpe <fhimpe@mandriva.org> 0.9.14-3mdv2009.1
+ Revision: 294509
- Sync with Debian patches:
  * Fix desktop file not to include encoding
  * Fix call to g_build_filename
  * Fix calls to synclients on locales using , instead of .
  * Fix docbook to be valid XML
  * Do not set undefined gconf values, it causes disabling of
    touchpad at GNOME startup (bug #40918)

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.9.14-2mdv2009.0
+ Revision: 266989
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun May 11 2008 Frederik Himpe <fhimpe@mandriva.org> 0.9.14-1mdv2009.0
+ Revision: 205850
- New version
- Adapt to new license policy

* Mon Feb 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.13-2mdv2008.1
+ Revision: 170076
- rebuild, due to package loss

* Fri Jan 11 2008 Olivier Blin <oblin@mandriva.com> 0.9.13-1mdv2008.1
+ Revision: 148022
- initial gsynaptics release
- create gsynaptics

