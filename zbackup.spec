Summary:        A globally-deduplicating backup tool
Name:           zbackup
Version:        1.3
Release:        1
License:        GPL v2+
Group:          Applications/Archiving
URL:            http://zbackup.org/
Source0:        https://github.com/zbackup/zbackup/archive/%{version}.tar.gz
BuildRequires:  cmake >= 2.8.2
BuildRequires:  openssl-devel
BuildRequires:  protobuf-devel
BuildRequires:  zlib-devel
BuildRequires:  xz-devel
BuildRoot:      %{_tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:       openssl
Requires:       protobuf
Requires:       zlib
Requires:       xz

%description
zbackup is a globally-deduplicating backup tool, based on the ideas
found in rsync. Feed a large .tar into it, and it will store duplicate
regions of it only once, then compress and optionally encrypt the
result. Feed another .tar file, and it will also re-use any data found
in any previous backups. This way only new changes are stored, and as
long as the files are not very different, the amount of storage
required is very low.

%prep
%setup -q

%build
cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/local/bin/%{name}

%changelog
* Fri Nov 28 2014 Daniele Viganò <daniele@vigano.me>
- bump to version 1.3
* Mon Apr 28 2014 Dmitriy Slupytskyi <dslupytskyi@gmail.com>
- added dependencies for install

