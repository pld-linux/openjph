Summary:	Open-source implementation of HTJ2K encoder and decoder
Summary(pl.UTF-8):	Implementacja kodera i dekodera HTJ2K o otwartych źródłach
Name:		openjph
Version:	0.31.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/aous72/OpenJPH/releases
Source0:	https://github.com/aous72/OpenJPH/archive/%{version}/OpenJPH-%{version}.tar.gz
# Source0-md5:	0648857971a89f1a0330607cedb47b94
Patch0:		%{name}-sse.patch
URL:		https://openjph.org/
BuildRequires:	cmake >= 3.12.0
BuildRequires:	gcc >= 6:4.7
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtiff-devel >= 4
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open source implementation of High-throughput JPEG2000 (HTJ2K), also
known as JPH, JPEG2000 Part 15, ISO/IEC 15444-15, and ITU-T T.814.
Here, we are interested in implementing the HTJ2K only, supporting
features that are defined in JPEG2000 Part 1 (for example, for wavelet
transform, only reversible 5/3 and irreversible 9/7 are supported).

%description -l pl.UTF-8
Mająca otwarte źródła implementacja standardu High-throughput JPEG2000
(HTJ2K), znanego także jako JPH, JPEG2000 Part 15, ISO/IEC 15444-15
tudzież ITU-T T.814. Tutaj zaimplementowano tylko HTJ2K z obsługą
właściwości zdefiniowanych w standardzie JPEG2000 Part 1 (np. dla
transformaty faletkowej obsługiwane są tylko odwracalna 5/3 oraz
nieodwracalna 9/7).

%package devel
Summary:	Header files for OpenJPH library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenJPH
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for OpenJPH library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenJPH.

%package tools
Summary:	Tools for encoding and decoding JPH files
Summary(pl.UTF-8):	Narzędzia do kodowania i dekodowania plików JPH
Group:		Applications/Graphics
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
Tools for encoding and decoding JPH files.

%description tools -l pl.UTF-8
Narzędzia do kodowania i dekodowania plików JPH.

%prep
%setup -q -n OpenJPH-%{version}
%patch -P0 -p1

%build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md docs/{status,usage_examples,web_demos}.md
%{_libdir}/libopenjph.so.*.*.*
%ghost %{_libdir}/libopenjph.so.0.31

%files devel
%defattr(644,root,root,755)
%{_libdir}/libopenjph.so
%{_includedir}/openjph
%{_pkgconfigdir}/openjph.pc
%{_libdir}/cmake/openjph

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ojph_compress
%attr(755,root,root) %{_bindir}/ojph_expand
