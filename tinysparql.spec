#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_with	icu		# libicu instead of libunistring
%bcond_with	static_libs	# static library
%bcond_without	vala		# Vala API

%define		abiver	3.0
Summary:	TinySPARQL - complete RDF triplestore with SPARQL 1.1 interface
Summary(pl.UTF-8):	TinySPARQL - pełna implementacja przechowywania trójek RDF z interfejsem SPARQL 1.1
Name:		tinysparql
Version:	3.8.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://download.gnome.org/sources/tinysparql/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	b265db81d1292d405945dbeb168a361b
URL:		https://gnome.pages.gitlab.gnome.org/tinysparql/
BuildRequires:	asciidoc
BuildRequires:	dbus-devel >= 1.3.1
BuildRequires:	gettext-tools
%{?with_apidocs:BuildRequires:	gi-docgen}
BuildRequires:	glib2-devel >= 1:2.52.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	json-glib-devel >= 1.4
%{?with_icu:BuildRequires:	libicu-devel >= 4.8.1.1}
BuildRequires:	libsoup3-devel >= 2.99.2
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
BuildRequires:	vala-libsoup3 >= 2.99.2
%{?with_apidocs:BuildRequires:	xmlto}
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:2.52.0
Requires(post,preun):	systemd-units >= 1:250.1
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus >= 1.3.1
Requires:	systemd-units >= 1:250.1
Provides:	tracker3 = %{version}-%{release}
Obsoletes:	tracker3 < 3.8
Obsoletes:	bash-completion-tracker3 < 3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The TinySPARQL library offers a complete RDF triplestore with SPARQL 1.1
interface and a minimal footprint. It allows creating local databases
in memory or the filesystem, and accessing/creating endpoints for
federated queries.

%description -l pl.UTF-8
Biblioteka TinySPARQL oferuje kompletny system przechowywania trójek
RDF z interfejsem SPARQL 1.1 i minimalnym narzutem. Pozwala tworzyć
bazy lokalne w pamięci lub systemie plików oraz końcówki
dostępowe/tworzące dla zapytań stowarzyszonych.

%package libs
Summary:	TinySPARQL: A SPARQL triple store library
Summary(pl.UTF-8):	TinySPARQL - biblioteka przechowywania trójek SPARQL
License:	LGPL v2.1+
Group:		Libraries
Requires:	glib2 >= 1:2.52.0
Requires:	json-glib >= 1.4
Requires:	libsoup3 >= 2.99.2
Requires:	libxml2 >= 1:2.6.31
Requires:	sqlite3-libs >= 3.35.2
Provides:	tracker3-libs = %{version}-%{release}
Obsoletes:	tracker3-libs < 3.8

%description libs
TinySPARQL: A SPARQL triple store library (formerly Tracker SPARQL
library).

%description libs -l pl.UTF-8
TinySPARQL - biblioteka przechowywania trójek SPARQL (dawniej
biblioteka Tracker SPARQL).

%package devel
Summary:	Header files for TinySPARQL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki TinySPARQL
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.52.0
Requires:	json-glib-devel >= 1.4
Requires:	libstemmer-devel
Requires:	libxml2-devel >= 1:2.6.31
Provides:	tracker3-devel = %{version}-%{release}
Obsoletes:	tracker3-devel < 3.8

%description devel
Header files for TinySPARQL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki TinySPARQL.

%package static
Summary:	Static TinySPARQL library
Summary(pl.UTF-8):	Statyczna biblioteka TinySPARQL
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	tracker3-static < 3.8

%description static
Static TinySPARQL library.

%description static -l pl.UTF-8
Statyczna biblioteka TinySPARQL.

%package apidocs
Summary:	TinySPARQL library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki TinySPARQL
Group:		Documentation
Obsoletes:	tracker3-apidocs < 3.8
BuildArch:	noarch

%description apidocs
TinySPARQL library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki TinySPARQL.

%package -n vala-tinysparql
Summary:	TinySPARQL/TrackerSPARQL 3 API for Vala language
Summary(pl.UTF-8):	API TinySPARQL/TrackerSPARQL 3 dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18.0
Provides:	vala-tracker3 = %{version}-%{release}
Obsoletes:	vala-tracker3 < 3.8
BuildArch:	noarch

%description -n vala-tinysparql
TinySPARQL/TrackerSPARQL 3 API for Vala language.

%description -n vala-tinysparql -l pl.UTF-8
API TinySPARQL/TrackerSPARQL 3 dla języka Vala.

%prep
%setup -q

%build
CPPFLAGS="%{rpmcppflags} -I/usr/include/libstemmer"
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	-Dbash_completion_dir=%{bash_compdir} \
	%{!?with_apidocs:-Ddocs=false} \
	-Dsystemd_user_services_dir=%{systemduserunitdir} \
	-Dunicode_support=%{?with_icu:icu}%{!?with_icu:unistring}

%ninja_build -C build -j1

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/Tsparql-* $RPM_BUILD_ROOT%{_gidocdir}
%endif

%find_lang tinysparql3

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_user_post tracker-xdg-portal-3.service

%preun
%systemd_user_preun tracker-xdg-portal-3.service

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f tinysparql3.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tinysparql
%attr(755,root,root) %{_libexecdir}/tinysparql-sql
%attr(755,root,root) %{_libexecdir}/tinysparql-xdg-portal-3
%{_datadir}/dbus-1/services/org.freedesktop.portal.Tracker.service
%{bash_compdir}/tinysparql
%{systemduserunitdir}/tinysparql-xdg-portal-3.service
%{_mandir}/man1/tinysparql-endpoint.1*
%{_mandir}/man1/tinysparql-export.1*
%{_mandir}/man1/tinysparql-import.1*
%{_mandir}/man1/tinysparql-introspect.1*
%{_mandir}/man1/tinysparql-query.1*
%{_mandir}/man1/tinysparql-sql.1*
%{_mandir}/man1/tinysparql-xdg-portal-3.1*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS COPYING MAINTAINERS NEWS README.md
%attr(755,root,root) %{_libdir}/libtinysparql-%{abiver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtinysparql-%{abiver}.so.0
# compat symlinks
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{abiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{abiver}.so.0
%{_libdir}/girepository-1.0/Tracker-%{abiver}.typelib
%{_libdir}/girepository-1.0/Tsparql-%{abiver}.typelib
%dir %{_libdir}/tinysparql-%{abiver}
%attr(755,root,root) %{_libdir}/tinysparql-%{abiver}/libtracker-http-soup3.so
%if %{with icu}
%attr(755,root,root) %{_libdir}/tinysparql-%{abiver}/libtracker-parser-libicu.so
%else
%attr(755,root,root) %{_libdir}/tinysparql-%{abiver}/libtracker-parser-libunistring.so
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtinysparql-%{abiver}.so
# compat symlink
%attr(755,root,root) %{_libdir}/libtracker-sparql-%{abiver}.so
%{_includedir}/tinysparql-%{abiver}
%{_pkgconfigdir}/tinysparql-%{abiver}.pc
%{_pkgconfigdir}/tracker-sparql-%{abiver}.pc
%{_datadir}/gir-1.0/Tracker-%{abiver}.gir
%{_datadir}/gir-1.0/Tsparql-%{abiver}.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtinysparql-%{abiver}.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/Tsparql-%{abiver}
%endif

%if %{with vala}
%files -n vala-tinysparql
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/tinysparql-%{abiver}.deps
%{_datadir}/vala/vapi/tinysparql-%{abiver}.vapi
%{_datadir}/vala/vapi/tracker-sparql-%{abiver}.deps
%{_datadir}/vala/vapi/tracker-sparql-%{abiver}.vapi
%endif
