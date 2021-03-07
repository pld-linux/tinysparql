#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_with	icu		# libicu instead of libunistring
%bcond_with	static_libs	# static libraries
%bcond_without	vala		# Vala API

%define		abiver	3.0
Summary:	Tracker 3 - an indexing subsystem
Summary(pl.UTF-8):	Tracker 3 - podsystem indeksujący
Name:		tracker3
Version:	3.0.3
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://download.gnome.org/sources/tracker/3.0/tracker-%{version}.tar.xz
# Source0-md5:	9ba66827bb5271c9e477980639d9873b
URL:		https://wiki.gnome.org/Projects/Tracker
BuildRequires:	asciidoc
BuildRequires:	dbus-devel >= 1.3.1
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.52.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	graphviz
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	json-glib-devel >= 1.0
%{?with_icu:BuildRequires:	libicu-devel >= 4.8.1.1}
BuildRequires:	libsoup-devel >= 2.40
BuildRequires:	libstemmer-devel
%{!?with_icu:BuildRequires:	libunistring-devel}
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.50
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	sqlite3-devel >= 3.29
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 2:0.18.0}
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:2.52.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 1.3.1
Requires:	systemd-units >= 1:242
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
Requires:	json-glib >= 1.0
Requires:	libsoup >= 2.40
Requires:	libxml2 >= 1:2.6.31
Requires:	sqlite3 >= 3.29

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
Requires:	json-glib-devel >= 1.0
Requires:	libsoup-devel >= 2.40
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
Requires:	gtk-doc-common
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
Requires:	bash-completion >= 2.0

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
	-Dfunctional_tests=false \
	-Dsystemd_user_services_dir=%{systemduserunitdir} \
	-Dunicode_support=%{?with_icu:icu}%{!?with_icu:unistring}

%ninja_build -C build -j1

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tracker-%{abiver}/libtracker-*.a
%endif

%find_lang tracker3

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f tracker3.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tracker3
%attr(755,root,root) %{_libexecdir}/tracker-xdg-portal-3
%dir %{_libexecdir}/tracker3
%attr(755,root,root) %{_libexecdir}/tracker3/endpoint
%attr(755,root,root) %{_libexecdir}/tracker3/export
%attr(755,root,root) %{_libexecdir}/tracker3/help
%attr(755,root,root) %{_libexecdir}/tracker3/import
%attr(755,root,root) %{_libexecdir}/tracker3/sparql
%attr(755,root,root) %{_libexecdir}/tracker3/sql
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
%dir %{_libdir}/tracker-%{abiver}
%dir %{_libdir}/tracker-%{abiver}/trackertestutils
%attr(755,root,root) %{_libdir}/tracker-%{abiver}/trackertestutils/tracker-sandbox
%{_libdir}/tracker-%{abiver}/trackertestutils/*.py
%{_pkgconfigdir}/tracker-testutils-%{abiver}.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libtracker-sparql-3
%{_gtkdocdir}/ontology-3
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
