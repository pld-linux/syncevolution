Summary:	Synchronization for contacts and calendars for Evolution
Summary(pl.UTF-8):	Synchronizacja kontaktów i kalendarzy dla Evolution
Name:		syncevolution
Version:	0.8.1
Release:	0.2
License:	GPL v2+ + OpenSSL exception
Group:		Applications
Source0:	http://www.estamos.de/download/syncevolution/sources/%{name}-%{version}.tar.gz
# Source0-md5:	c2a38265fd0619a09e2f2154d37ba54f
URL:		http://www.estamos.de/projects/SyncML/SyncEvolution.html
BuildRequires:	curl-devel
BuildRequires:	evolution-data-server-devel
#BuildRequires:	funambol-devel - currently uses bundled copy
BuildRequires:	glib2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	sqlite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q

%build
%configure \
	--enable-ebook \
	--enable-ecal \
	--enable-file \
	--enable-sqlite \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/syncevolution/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains additional notes
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/synccompare
%attr(755,root,root) %{_bindir}/syncevolution
%dir %{_libdir}/syncevolution
%attr(755,root,root) %{_libdir}/syncevolution/libsyncevolution.so
%attr(755,root,root) %{_libdir}/syncevolution/libsyncevolution.so.0
%attr(755,root,root) %{_libdir}/syncevolution/libsyncevolution.so.0.0.0
%attr(755,root,root) %{_libdir}/syncevolution/syncaddressbook.so
%attr(755,root,root) %{_libdir}/syncevolution/syncaddressbook.so.0
%attr(755,root,root) %{_libdir}/syncevolution/syncaddressbook.so.0.0.0
%attr(755,root,root) %{_libdir}/syncevolution/syncebook.so
%attr(755,root,root) %{_libdir}/syncevolution/syncebook.so.0
%attr(755,root,root) %{_libdir}/syncevolution/syncebook.so.0.0.0
%attr(755,root,root) %{_libdir}/syncevolution/syncecal.so
%attr(755,root,root) %{_libdir}/syncevolution/syncecal.so.0
%attr(755,root,root) %{_libdir}/syncevolution/syncecal.so.0.0.0
%attr(755,root,root) %{_libdir}/syncevolution/syncfile.so
%attr(755,root,root) %{_libdir}/syncevolution/syncfile.so.0
%attr(755,root,root) %{_libdir}/syncevolution/syncfile.so.0.0.0
%attr(755,root,root) %{_libdir}/syncevolution/syncsqlite.so
%attr(755,root,root) %{_libdir}/syncevolution/syncsqlite.so.0
%attr(755,root,root) %{_libdir}/syncevolution/syncsqlite.so.0.0.0
