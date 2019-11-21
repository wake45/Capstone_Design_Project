---
layout: post
title:  "Docker[Online Judge]"
summary: "Docker 설치하고 온라인 저지 실행시키기"
date:   2019-03-22 18:00 -0400
categories: capston
---

# docker
- 컨테이너 기반 가상머신
- 만들어진 이미지를 이용해서 동작한다.
- 매우 가볍다.

기존의 Virtual Machine과 비슷하게 동작하지만 자신의 OS에 app을 올리는 것이 아니라 docker engine에 app을 올리기 때문에 더 가볍게 동작할 수 있다. 기존의 Virtual Machine은 app을 동작시키기위해 가상환경을 구축하고 배포하는데 시간이 걸리지만 docker를 이용하면 가상환경을 간단하게 구축해서 간단한 app을 동작시키게 할 수 있기 때문에 많이 사용된다. 여러 환경에 app을 구동해서 connection 하는게 간편한게 장점이다.

# docker compose
- docker를 묶은거

## docker

- [https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html)

## docker compose

- [http://avilos.codes/infra-management/virtualization-platform/docker/docker-compose/](http://avilos.codes/infra-management/virtualization-platform/docker/docker-compose/)

## docker 자주쓰는 명령어

- 이미지 확인

```
docker images
```

- 이미지 삭제

```
docker rmi <image name>
```

- none 이미지 전부삭제

```
docker rmi $(docker images -f "dangling=true" -q)
```

- docker 캐시 비우기

```
docker system prune -a
```
- docker 목록

```
docker ps
```

- docker 중지,삭제

```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

---

# Online Judge

- [깃허브](https://github.com/QingdaoU/OnlineJudgeDeploy/tree/2.0)를 참조합니다.

- 도커설치

```
sudo apt-get update && sudo apt-get install -y vim python-pip curl git
pip install docker-compose
sudo curl -sSL get.docker.com | sh
```

- 설치 확인

```
docker version
```

- git 가져오기

```
git clone -b 2.0 https://github.com/QingdaoU/OnlineJudgeDeploy.git && cd OnlineJudgeDeploy
```

- 설치 진행(둘중 하나)

```
docker-compose up -d //일반
sudo -E docker-compose up -d //권한
```

- 실행이 잘된다.. GOOD

- docker ps



![ps](https://github.com/jjeamin/jjeamin.github.io/raw/master/_posts/post_img/capston/ps.PNG)



- 여러가지 도커 컨테이너들이 동작하고 있습니다.

웹 브라우저를 통해 서버의 HTTP 80 포트 또는 HTTPS 443 포트를 방문하면 시작됩니다.백그라운드 관리 경로는 /admin이며 설치 중에 자동으로 추가된 슈퍼 관리자 사용자 이름은 root이고 암호는 rootroot이므로 반드시 적시에 암호를 수정하세요.

**[여기](https://docs.onlinejudge.me/#/onlinejudge/guide/deploy) 문서를 읽어야합니다.** 중국어로 되어있어서 옆에는 파파고 번역기 켜놓고 변역해서 봤습니다.


# 참조
- [https://github.com/QingdaoU/OnlineJudgeDeploy/tree/2.0](https://github.com/QingdaoU/OnlineJudgeDeploy/tree/2.0)
- [https://docs.onlinejudge.me/#/](https://docs.onlinejudge.me/#/)
