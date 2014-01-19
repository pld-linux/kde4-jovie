#
%define		_state		stable
%define		orgname		jovie
%define		qtver		4.8.0

Summary:	K Desktop Environment - KDE text to speech system application
Name:		kde4-jovie
Version:	4.12.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	1ca7323e0ab8a911830ecbda80ec0e41
URL:		http://www.kde.org/
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	speech-dispatcher-devel
Requires:	kde4-kdebase-workspace >= 4.11.4
Obsoletes:	kde4-kdeaccessibility-jovie
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jovie is the KDE text to speech system application.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jovie
%attr(755,root,root) %{_libdir}/kde4/jovie_stringreplacerplugin.so
%attr(755,root,root) %{_libdir}/kde4/jovie_talkerchooserplugin.so
%attr(755,root,root) %{_libdir}/kde4/jovie_xmltransformerplugin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kttsd.so
%attr(755,root,root) %{_libdir}/libkttsd.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkttsd.so.?
%{_datadir}/apps/jovie
#%{_datadir}/apps/kttsd
%{_datadir}/kde4/services/jovie.desktop
%{_datadir}/kde4/services/jovie_stringreplacerplugin.desktop
%{_datadir}/kde4/services/jovie_talkerchooserplugin.desktop
%{_datadir}/kde4/services/jovie_xmltransformerplugin.desktop
%{_datadir}/kde4/services/kcmkttsd.desktop
%{_datadir}/kde4/services/kttsd.desktop
%{_datadir}/kde4/servicetypes/jovie_filterplugin.desktop
%{_desktopdir}/kde4/jovieapp.desktop
%{_iconsdir}/hicolor/*/actions/speak.png
%{_iconsdir}/hicolor/*/actions/nospeak.png
%{_iconsdir}/hicolor/*/actions/male.png
%{_iconsdir}/hicolor/*/actions/female.png
