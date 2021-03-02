Name: test
Version: 0.0.1
Release: 1%{?dist}
Summary: Test

License: GPLv3
URL: https://github.com/mmuzila/test
Source0: test.txt

%description
Just for test purposes

%install
cp test.txt %{buildroot}%{_datadir}

%files
%{_datadir)/test.txt

%changelog
* Mon Mar 01 2021 Matej Mužila <mmuzila@redhat.com> - 0.0.1-1
- Init
