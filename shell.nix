let pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  buildInputs = with pkgs.python37Packages; [
    tkinter
    pip
    numpy
    pycodestyle
    matplotlib
    pillow
  ];
  shellHook = ''
            alias pip3="PIP_PREFIX='$(pwd)/_build/pip_packages' \pip3"
            export PYTHONPATH="$(pwd)/_build/pip_packages/lib/python3.7/site-packages:$PYTHONPATH"
            unset SOURCE_DATE_EPOCH
  '';
}
