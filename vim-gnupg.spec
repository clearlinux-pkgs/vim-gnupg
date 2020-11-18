#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vim-gnupg
Version  : 2.7.1
Release  : 3
URL      : https://github.com/jamessan/vim-gnupg/archive/v2.7.1/vim-gnupg-2.7.1.tar.gz
Source0  : https://github.com/jamessan/vim-gnupg/archive/v2.7.1/vim-gnupg-2.7.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Vim
Requires: vim-gnupg-data = %{version}-%{release}
Patch1: build.patch

%description
# vim-gnupg
This script implements transparent editing of gpg encrypted files. The filename
must have a `.gpg`, `.pgp` or `.asc` suffix. When opening such a file the
content is decrypted, when opening a new file the script will ask for the
recipients of the encrypted file. The file content will be encrypted to all
recipients before it is written. The script turns off viminfo, swapfile, and
undofile to increase security.

%package data
Summary: data components for the vim-gnupg package.
Group: Data

%description data
data components for the vim-gnupg package.


%prep
%setup -q -n vim-gnupg-2.7.1
cd %{_builddir}/vim-gnupg-2.7.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605722336
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1605722336
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/vim/addons/plugin/gnupg.vim
