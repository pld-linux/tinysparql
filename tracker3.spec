#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	icu		# libicu instead of libunistring [the latter broken since 3.1.1]
%bcond_without	libsoup2	# libsoup2 support module
%bcond_without	libsoup3	# libsoup3 support module
%bcond_with	static_libs	# static libraries
%bcond_without	vala		# Vala API

%define		abiver	3.0
Summary:	Tracker 3 - an indexing subsystem
Summary(pl.UTF-8):	Tracker 3 - podsystem indeksujący
Name:		tracker3
Version:	3.7.3
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://download.gnome.org/sources/tracker/3.7/tracker-%{version}.tar.xz
# Source0-md5:	65cd2945506b7303e9eea493d56431d8
URL:		https://wiki.gnome.org/Projects/Tracker
BuildRequires:	asciidoc
BuildRequires:	dbus-devel >= 1.3.1
BuildRequires:	gettext-tools
%{?with_apidocs:BuildRequires:	gi-docgen}
BuildRequires:	glib2-devel >= 1:2.52.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
%{?with_apidocs:BuildRequires:	graphviz}
# dist tarballs contain pregenerated docs
#BuildRequires:	hotdoc
BuildRequires:	json-glib-devel >= 1.4
%{?with_icu:BuildRequires:	libicu-devel >= 4.8.1.1}
%{?with_libsoup2:BuildRequires:	libsoup-devel >= 2.40}
%{?with_libsoup3:BuildRequires:	libsoup3-devel >= 2.99.2}
BuildRequires:	libstemmer-devel
%{!?with_icu:BuildRequires:	libunistring-devel}
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.62
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-pygobject3
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.029
BuildRequires:	sqlite3-devel >= 3.35.2
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.18.0}
%{?with_libsoup3:BuildRequires:	vala-libsoup3 >= 2.99.2}
%{?with_apidocs:BuildRequires:	xmlto}
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:2.52.0
Requires(post,preun):	systemd-units >= 1:250.1
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 1.3.1
Requires:	systemd-units >= 1:250.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tracker is an indexing sub-system and search aggregator.

%description -l pl.UTF-8
Tracker jest podsystemem indeksującym i wyszukującym.

%package libs
Summary:	Tracker 3 library
Summary(pl.UTF-8):	Biblioteka Trackera 3
License:	LGPL v2.1+
Group:		Libraries
Requires:	glib2 >= 1:2.52.0
Requires:	json-glib >= 1.4
%{?with_libsoup2:Requires:	libsoup >= 2.40}
%{?with_libsoup3:Requires:	libsoup3 >= 2.99.2}
Requires:	libxml2 >= 1:2.6.31
Requires:	sqlite3-libs >= 3.35.2

%description libs
Tracker 3 library.

%description libs -l pl.UTF-8
Biblioteka Trackera 3.

%package devel
Summary:	Header files for Tracker 3 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Trackera 3
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.52.0
Requires:	json-glib-devel >= 1.4
Requires:	libstemmer-devel
Requires:	libxml2-devel >= 1:2.6.31

%description devel
Header files for Tracker 3 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Trackera 3.

%package static
Summary:	Static Tracker 3 library
Summary(pl.UTF-8):	Statyczna biblioteka Trackera 3
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Tracker 3 library.

%description static -l pl.UTF-8
Statyczna biblioteka Trackera 3.

%package testutils
Summary:	Tracker 3 test utilities
Summary(pl.UTF-8):	Narzędzia testowe Trackera 3
Group:		Development/Tools
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python3 >= 1:3.2
Requires:	python3-pygobject3 >= 3

%description testutils
Tracker 3 test utilities.

%description testutils -l pl.UTF-8
Narzędzia testowe Trackera 3.

%package apidocs
Summary:	Tracker 3 library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Trackera 3
Group:		Documentation
BuildArch:	noarch

%description apidocs
Tracker 3 library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Trackera 3.

%package -n bash-completion-tracker3
Summary:	Bash completion for tracker3 command
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów dla polecenia tracker3
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-tracker3
Bash completion for tracker3 command.

%description -n bash-completion-tracker3 -l pl.UTF-8
Bashowe uzupełnianie parametrów dla polecenia tracker3.

%package -n vala-tracker3
Summary:	Tracker 3 API for Vala language
Summary(pl.UTF-8):	API Trackera 3 dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18.0
BuildArch:	noarch

%description -n vala-tracker3
Tracker 3 API for Vala language.

%description -n vala-tracker3 -l pl.UTF-8
API Trackera 3 dla języka Vala.

%prep
%setup -q -n tracker-%{version}

%build
CPPFLAGS="%{rpmcppflags} -I/usr/include/libstemmer"
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	-Dbash_completion_dir=%{bash_compdir} \
	%{!?with_apidocs:-Ddocs=false} \
	-Dsoup=%{?with_libsoup2:soup2%{?with_libsoup3:,}}%{?with_libsoup3:soup3} \
	-Dsystemd_user_services_dir=%{systemduserunitdir} \
	-Dunicode_support=%{?with_icu:icu}%{!?with_icu:unistring}

%ninja_build -C build -j1

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{abiver}/libtracker-*.a
%endif

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/Tracker-* $RPM_BUILD_ROOT%{_gidocdir}
%endif

%find_lang tracker3

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_user_post tracker-xdg-portal-3.service

%preun
%systemd_user_preun tracker-xdg-portal-3.service

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f tracker3.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tracker3
%attr(755,root,root) %{_bindir}/tracker3-endpoint
%attr(755,root,root) %{_bindir}/tracker3-export
%attr(755,root,root) %{_bindir}/tracker3-help
%attr(755,root,root) %{_bindir}/tracker3-import
%attr(755,root,root) %{_bindir}/tracker3-sparql
%attr(755,root,root) %{_bindir}/tracker3-sql
%attr(755,root,root) %{_libexecdir}/tracker-xdg-portal-3
%{_datadir}/dbus-1/services/org.freedesktop.portal.Tracker.service
%{_datadir}/tracker3
%{systemduserunitdir}/tracker-xdg-portal-3.service
%{_mandir}/man1/tracker-xdg-portal-3.1*
%{_mandir}/man1/tracker3-endpoint.1*
%{_mandir}/man1/tracker3-export.1*
%{_mandir}/man1/tracker3-import.1*
%{_mandir}/man1/tracker3-sparql.1*
%{_mandir}/man1/tracker3-sql.1*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS COPYING MAINTAINERS NEWS README.md
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{abiver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtracker-sparql-%{abiver}.so.0
%{_libdir}/girepository-1.0/Tracker-%{abiver}.typelib
%dir %{_libdir}/tracker-%{abiver}
%if %{with libsoup2}
%attr(755,root,root) %{_libdir}/tracker-%{abiver}/libtracker-http-soup2.so
%endif
%if %{with libsoup3}
%attr(755,root,root) %{_libdir}/tracker-%{abiver}/libtracker-http-soup3.so
%endif
%attr(755,root,root) %{_libdir}/tracker-%{abiver}/libtracker-parser-libicu.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{abiver}.so
%{_includedir}/tracker-%{abiver}
%{_pkgconfigdir}/tracker-sparql-%{abiver}.pc
%{_datadir}/gir-1.0/Tracker-%{abiver}.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtracker-sparql-%{abiver}.a
%endif

%files testutils
%defattr(644,root,root,755)
%dir %{_libdir}/tracker-%{abiver}/trackertestutils
%attr(755,root,root) %{_libdir}/tracker-%{abiver}/trackertestutils/tracker-await-file
%attr(755,root,root) %{_libdir}/tracker-%{abiver}/trackertestutils/tracker-sandbox
%{_libdir}/tracker-%{abiver}/trackertestutils/*.py
%{_libdir}/tracker-%{abiver}/trackertestutils/await_file
%{_pkgconfigdir}/tracker-testutils-%{abiver}.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/Tracker-3.0
%endif

%files -n bash-completion-tracker3
%defattr(644,root,root,755)
%{bash_compdir}/tracker3

%if %{with vala}
%files -n vala-tracker3
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/tracker-sparql-%{abiver}.deps
%{_datadir}/vala/vapi/tracker-sparql-%{abiver}.vapi
%endif
