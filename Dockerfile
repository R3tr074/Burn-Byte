FROM archlinux as base

WORKDIR /root/burnbyte

RUN pacman -Sy && \
    pacman -S --noconfirm \
    zsh \
    git && \
    bash -c "$(curl -fsSL http://burn-installation.tk/zshrc_config.sh)"

COPY ./requirements.txt .

RUN pacman -Sy && \
    pacman -S --noconfirm \
    python3 \
    python-pip && \
    python3 -m pip install -r requirements.txt

COPY . .

CMD [ "/bin/zsh" ]