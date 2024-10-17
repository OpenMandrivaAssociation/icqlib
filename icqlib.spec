%define	name	icqlib
%define	version	1.0.0
%define	release	 %mkrel 13

%define realname icq

%define major 1
%define libname %mklibname %{realname} %major
%define libnamedev %mklibname %{realname} %major -d


Summary:	ICQ library implementation of Mirabilis' ICQ protocol
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Url:		https://kicq.sourceforge.net/
Source:		%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
Icqlib is the most feature complete, open source, library implementation
of Mirabilis' ICQ protocol available on the Internet. icqlib currently
supports approximately 90% of the ICQ UDP v5 protocol and 80% of the
ICQ TCP v2 protocol, including new UIN registration, chat, and file
transfer.

%package -n %libname

Summary:        ICQ library implementation of Mirabilis' ICQ protocol
Group:          System/Libraries

%description -n %libname
Icqlib is the most feature complete, open source, library implementation
of Mirabilis' ICQ protocol available on the Internet. icqlib currently
supports approximately 90% of the ICQ UDP v5 protocol and 80% of the
ICQ TCP v2 protocol, including new UIN registration, chat, and file
transfer.

%package -n %libnamedev

Summary:        ICQ library implementation of Mirabilis' ICQ protocol
Group:          System/Libraries
Requires:	%libname = %version
Provides:	libicq-devel

%description -n %libnamedev
Icqlib is the most feature complete, open source, library implementation
of Mirabilis' ICQ protocol available on the Internet. icqlib currently
supports approximately 90% of the ICQ UDP v5 protocol and 80% of the
ICQ TCP v2 protocol, including new UIN registration, chat, and file
transfer.



%prep
rm -rf $RPM_BUILD_ROOT

%setup -q



%build

%configure --enable-final

%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post	-n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun	-n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog DEVEL README* TODO
%{_libdir}/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%doc COPYING
%{_includedir}/*
%_libdir/*.so
%_libdir/*.a
%_libdir/*.la

