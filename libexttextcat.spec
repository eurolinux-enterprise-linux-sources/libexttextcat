Name: libexttextcat
Version: 3.4.1
Release: 3%{?dist}
Summary: Text categorization library

Group: System Environment/Libraries
License: BSD
URL: http://www.freedesktop.org/wiki/Software/libexttextcat
Source: http://dev-www.libreoffice.org/src/libexttextcat/%{name}-%{version}.tar.xz

Obsoletes: libtextcat < 3.2.0
Provides: libtextcat = %{version}

%description
%{name} is an N-Gram-Based Text Categorization library primarily
intended for language guessing.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: libtextcat-devel < 3.2.0
Provides: libtextcat-devel = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Tool for creating custom document fingerprints
Group: Applications/Publishing
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains the createfp program that allows
you to easily create your own document fingerprints.


%prep
%setup -q


%build
%configure --disable-silent-rules --disable-static --disable-werror
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la


%check
make check


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc ChangeLog LICENSE README*
%{_libdir}/%{name}*.so.*
%{_datadir}/%{name}


%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/vala/vapi/libexttextcat.vapi


%files tools
%{_bindir}/createfp


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.4.1-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.4.1-2
- Mass rebuild 2013-12-27

* Thu May 30 2013 David Tardon <dtardon@redhat.com> - 3.4.1-1
- new release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Caolán McNamara <caolanm@redhat.com> 3.4.0-1
- latest import

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 David Tardon <dtardon@redhat.com> 3.3.1-1
- latest import

* Fri May 25 2012 Caolán McNamara <caolanm@redhat.com> 3.3.0-1
- latest version

* Tue Jan 24 2012 David Tardon <dtardon@redhat.com> 3.2.0-1
- initial import
