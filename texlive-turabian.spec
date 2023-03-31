Name:		texlive-turabian
Version:	36298
Release:	2
Summary:	Create Turabian-formatted material using LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/turabian
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turabian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turabian.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides a class file and a template for creating
Turabian-formatted projects. The class file supports citation
formatting conforming to the Turabian 8th Edition style guide.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/turabian
%doc %{_texmfdistdir}/doc/latex/turabian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
