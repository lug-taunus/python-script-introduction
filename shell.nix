let
  sources = import ./nix/sources.nix {};
  pkgs = import sources.nixpkgs {};
  poetry2nix = import sources.poetry2nix {inherit pkgs;};
  envShell = poetry2nix.mkPoetryEnv {
    projectDir = ./.;
    groups = [];
    checkGroups = [];
  };
in
  pkgs.mkShell {
    packages = with pkgs; [
      niv # Manage Nix dependencies
      python3
      poetry
      ruff

      envShell
    ];
  }
