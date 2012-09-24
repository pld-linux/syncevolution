#
Summary:	Synchronization for contacts and calendars for Evolution
Summary(pl.UTF-8):	Synchronizacja kontaktów i kalendarzy dla Evolution
Name:		syncevolution
Version:	1.3
Release:	0.1
License:	GPL v2+ + OpenSSL exception
Group:		Applications
Source0:	http://downloads.syncevolution.org/syncevolution/sources/%{name}-%{version}.tar.gz
# Source0-md5:	db25bf5b95ce2125cbde17344377203f
URL:		https://syncevolution.org/
BuildRequires:	boost-devel >= 1.34
BuildRequires:	curl-devel
BuildRequires:	docutils
BuildRequires:	evolution-data-server-devel
#BuildRequires:	funambol-devel - currently uses bundled copy
BuildRequires:	glib2-devel
BuildRequires:	libgdata-devel
BuildRequires:	libproxy-devel
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	specflags	-fPIC

%description
SyncEvolution synchronizes personal information management (PIM) data
like contacts, calenders, tasks and memos via the SyncML information
synchronization standard. It supports all of these for GNOME's
Evolution and contacts for the system address book of the Nokia
Internet Tablets, Mac OS X and the iPhone.

The command-line tool 'syncevolution' (compiled separately for each of
these platforms) executes the synchronization. The project 'Genesis'
(available separately) provides a graphical user interface.

%description -l pl.UTF-8
Synchronizacja kontaktów i kalendarzy dla Evolution.

%package libs
Summary:	Syncevolution libraries
Summary(pl.UTF-8):	Biblioteki Syncevolution
Group:		Libraries

%description libs
Syncevolution shared libraries.

%description libs -l pl.UTF-8
Biblioteki dzielone Syncevolution.

%package static
Summary:	Syncevolution static libs
Summary(pl.UTF-8):	Biblioteki statyczne Syncevolution
Group:		Libraries

%description static
Syncevolution static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Syncevolution.

%package devel
Summary:	Header files for Syncevolution libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Syncevolution
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Syncevolution libraries

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Syncevolution.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4 -I m4-repo
%{__autoconf}
%{__autoheader}
%{__automake}
cd src/synthesis
%{__libtoolize}
%{__aclocal} -I m4 -I ../../m4-repo
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../..
%configure \
	--enable-shared \
	--enable-evolution-compatibility

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/syncevolution/backends/*.{la,a}
%{__rm} $RPM_BUILD_ROOT%{_datadir}/syncevolution/templates/README
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/syncevolution

%post -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains additional notes
%doc AUTHORS COPYING ChangeLog NEWS README test/README.*
%dir %{_datadir}/syncevolution
%dir %{_datadir}/syncevolution/templates
%dir %{_datadir}/syncevolution/templates/clients
%{_datadir}/syncevolution/templates/clients/*
%dir %{_datadir}/syncevolution/templates/contexts
%{_datadir}/syncevolution/templates/contexts/*
%dir %{_datadir}/syncevolution/templates/servers
%{_datadir}/syncevolution/templates/servers/*
%dir %{_datadir}/syncevolution/xml
%{_datadir}/syncevolution/xml/*.xml
%attr(755,root,root) %{_datadir}/syncevolution/xml/*.pl
%dir %{_datadir}/syncevolution/xml/datatypes
%{_datadir}/syncevolution/xml/datatypes/*
%dir %{_datadir}/syncevolution/xml/debug
%{_datadir}/syncevolution/xml/debug/*
%dir %{_datadir}/syncevolution/xml/remoterules
%{_datadir}/syncevolution/xml/remoterules/*.xml
%dir %{_datadir}/syncevolution/xml/remoterules/client
%{_datadir}/syncevolution/xml/remoterules/client/*
%dir %{_datadir}/syncevolution/xml/remoterules/server
%{_datadir}/syncevolution/xml/remoterules/server/*
%dir %{_datadir}/syncevolution/xml/scripting
%{_datadir}/syncevolution/xml/scripting/*
%attr(755,root,root) %{_bindir}/synccompare
%attr(755,root,root) %{_bindir}/syncevolution
%attr(755,root,root) %{_bindir}/syncevo-phone-config
%attr(755,root,root) %{_bindir}/synclog2html
%attr(755,root,root) %{_libdir}/syncevo-local-sync
%{_mandir}/man1/*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgdbussyncevo.so.0
%attr(755,root,root) %ghost %{_libdir}/libsmltk.so.0
%attr(755,root,root) %ghost %{_libdir}/libsyncevolution.so.0
%attr(755,root,root) %ghost %{_libdir}/libsynthesis.so.0
%attr(755,root,root) %{_libdir}/libgdbussyncevo.so.0.*
%attr(755,root,root) %{_libdir}/libsmltk.so.0.*
%attr(755,root,root) %{_libdir}/libsyncevolution.so.0.*
%attr(755,root,root) %{_libdir}/libsynthesis.so.0.*
%dir %{_libdir}/syncevolution
%dir %{_libdir}/syncevolution/backends
%attr(755,root,root) %{_libdir}/syncevolution/backends/platformgnome.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/platformkde.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncactivesync.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncaddressbook.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncakonadi.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncdav.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncebook.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncecal.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncfile.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/synckcalextended.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncmaemocal.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncqtcontacts.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncsqlite.so
%attr(755,root,root) %{_libdir}/syncevolution/backends/syncxmlrpc.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgdbussyncevo.so
%{_libdir}/libsmltk.so
%{_libdir}/libsyncevolution.so
%{_libdir}/libsynthesis.so
%{_includedir}/syncevo
%{_includedir}/synthesis
%{_pkgconfigdir}/syncevolution.pc
%{_pkgconfigdir}/synthesis-sdk.pc
%{_pkgconfigdir}/synthesis.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdbussyncevo.a
%{_libdir}/libsmltk.a
%{_libdir}/libsyncevolution.a
%{_libdir}/libsynthesis.a
