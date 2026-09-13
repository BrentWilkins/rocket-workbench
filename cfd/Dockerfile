# Native ARM64 CFD environment. Record built image ID and dpkg manifest per run.
FROM ubuntu:24.04@sha256:561618e2c15bf2397621dd04f96926663a3b5616c189cf7e38db7e82f5c538ea
COPY zz-openfoam-tutorials /etc/dpkg/dpkg.cfg.d/zz-openfoam-tutorials
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    openfoam=1912.200626-2build3 openfoam-examples=1912.200626-2build3 \
    && apt-get clean
WORKDIR /case
ENV WM_PROJECT_DIR=/usr/share/openfoam FOAM_ETC=/usr/share/openfoam/etc WM_PROJECT_VERSION=v1912
ENTRYPOINT ["/bin/bash", "-lc"]
