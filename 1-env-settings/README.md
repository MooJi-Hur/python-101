# Env Settings

## Conda 
### 가상환경
- venv와 conda
- 리눅스 버전이 업데이트 된 이후, 가상환경이 있어야 파이썬을 설치할 수 있음

### Miniconda 설치
- [홈페이지](https://www.anaconda.com/)
- Install for Just Me / All Users -> 설치 위치 차이
- [공식 문서](https://www.anaconda.com/docs/main)

### 설치 명령어
```bash
conda create --name multi01 python
```

- 환경변수는 명령어를 설치한 폴더 바깥에서도 사용할 수 있도록 기재해둔 경로
    ```bash
    % whereis conda
    conda: /opt/miniconda3/bin/conda
    ```
- 환경변수를 설정했음에도 `conda` 명령어를 인식하지 못한 경우 터미널을 재시작


### 설치 과정
- 약관 동의 -> 패키지 적용 내용 계획 확인 -> 설치


```bash
Do you accept the Terms of Service (ToS) for https://repo.anaconda.com/pkgs/main? [(a)ccept/(r)eject/(v)iew]: a
Do you accept the Terms of Service (ToS) for https://repo.anaconda.com/pkgs/r? [(a)ccept/(r)eject/(v)iew]: a
2 channel Terms of Service accepted
Retrieving notices: done
Channels:
 - defaults
Platform: osx-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /opt/miniconda3/envs/multi01

  added / updated specs:
    - python


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    pip-25.2                   |     pyhc872135_0         1.2 MB
    ------------------------------------------------------------
                                           Total:         1.2 MB

The following NEW packages will be INSTALLED:

  bzip2              pkgs/main/osx-64::bzip2-1.0.8-h6c40b1e_6 
  ca-certificates    pkgs/main/osx-64::ca-certificates-2025.7.15-hecd8cb5_0 
  expat              pkgs/main/osx-64::expat-2.7.1-h6d0c2b6_0 
  libcxx             pkgs/main/osx-64::libcxx-19.1.7-haebbb44_3 
  libffi             pkgs/main/osx-64::libffi-3.4.4-hecd8cb5_1 
  libmpdec           pkgs/main/osx-64::libmpdec-4.0.0-h46256e1_0 
  ncurses            pkgs/main/osx-64::ncurses-6.5-h923df54_0 
  openssl            pkgs/main/osx-64::openssl-3.0.17-hee2dfae_0 
  pip                pkgs/main/noarch::pip-25.2-pyhc872135_0 
  python             pkgs/main/osx-64::python-3.13.5-h81a7116_100_cp313 
  python_abi         pkgs/main/osx-64::python_abi-3.13-0_cp313 
  readline           pkgs/main/osx-64::readline-8.3-h49f2429_0 
  setuptools         pkgs/main/osx-64::setuptools-78.1.1-py313hecd8cb5_0 
  sqlite             pkgs/main/osx-64::sqlite-3.50.2-hc8b0dd6_1 
  tk                 pkgs/main/osx-64::tk-8.6.15-h3a5a201_0 
  tzdata             pkgs/main/noarch::tzdata-2025b-h04d1e81_0 
  wheel              pkgs/main/osx-64::wheel-0.45.1-py313hecd8cb5_0 
  xz                 pkgs/main/osx-64::xz-5.6.4-h46256e1_1 
  zlib               pkgs/main/osx-64::zlib-1.2.13-h4b97444_1 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                         
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate multi01
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

## Python
- [홈페이지](https://www.python.org/)
- [공식 문서](https://docs.python.org/)

### 파이썬 언어 참조 문서
- https://docs.python.org/3.13/reference/index.html#the-python-language-reference
- https://docs.python.org/3.13/reference/lexical_analysis.html
- https://docs.python.org/3.13/reference/lexical_analysis.html#encoding-declarations

### 라이브러리 참조 문서
- https://docs.python.org/3.13/library/index.html
- [Python Package Index](https://pypi.org/)



