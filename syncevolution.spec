#
Summary:	Synchronization for contacts and calendars for Evolution
Summary(pl.UTF-8):	Synchronizacja kontaktów i kalendarzy dla Evolution
Name:		syncevolution
Version:	0.9.2
Release:	1
License:	GPL v2+ + OpenSSL exception
Group:		Applications
Source0:	http://downloads.syncevolution.org/syncevolution/sources/%{name}-%{version}.tar.gz
# Source0-md5:	7716078e849bb4a01f5908872b46f015
URL:		http://www.estamos.de/projects/SyncML/SyncEvolution.html
BuildRequires:	boost-devel >= 1.34
BuildRequires:	curl-devel
BuildRequires:	evolution-data-server-devel
#BuildRequires:	funambol-devel - currently uses bundled copy
BuildRequires:	glib2-devel
BuildRequires:	libstdc++-devel
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
%configure \
	--enable-ebook \
	--enable-ecal \
	--enable-file \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/syncevolution/backends/*.la
rm -f $RPM_BUILD_ROOT%{_datadir}/syncevolution/templates/README
rm -rf $RPM_BUILD_ROOT%{_docdir}/syncevolution

%post -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains additional notes
%doc AUTHORS COPYING ChangeLog NEWS README test/README.*
%dir %{_datadir}/syncevolution
%dir %{_datadir}/syncevolution/templates
%dir %{_datadir}/syncevolution/templates/Funambol
%{_datadir}/syncevolution/templates/Funambol/*
%dir %{_datadir}/syncevolution/templates/ScheduleWorld
%{_datadir}/syncevolution/templates/ScheduleWorld/*
%attr(755,root,root) %{_bindir}/synccompare
%attr(755,root,root) %{_bindir}/syncevolution

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost  %{_libdir}/lib*.so.0
%attr(755,root,root) %{_libdir}/lib*.so.0.*
%dir %{_libdir}/syncevolution
%dir %{_libdir}/syncevolution/backends
%attr(755,root,root) %{_libdir}/syncevolution/backends/*.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
