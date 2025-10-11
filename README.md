# 📝[2025년 한이음 드림업 공모전 템플릿]
- 이 파일은 2025년 한이음 드림업 프로젝트를 수행하는 학생들에게 README 작성의 가이드라인을 제공하기 위해 제작되었습니다.
- [Git & Github 기초사용법 알아보기](https://github.com/hanium-dreamup-challenge/git_guide/blob/main/README_git_guide.md)
---
## **💡README 작성방법**
- 프로젝트에서 사용되는 소스코드를 레포지토리에 업로드 한 후, 아래 가이드에 따라 README.md파일을 작성해주세요.
- 필수 작성 항목(5가지) : 프로젝트 개요, 팀원 소개, 시스템 구성도, 작품 소개영상, 핵심 소스코드 
- 프로젝트 저장소명 규칙 : `https://github.com/깃허브계정명/프로젝트 번호`
- 예시) 깃허브 계정이 hanium이고, 프로젝트 번호가 25_HC001일 경우 -> `https://github.com/hanium/25_HC001`
- 아래 항목 및 내용은 이해를 돕기위한 예시입니다. 참고만 하되 자유롭게 추가 및 작성해주시기 바랍니다.

---

## **💡1. 프로젝트 개요**

**1-1. 프로젝트 소개**
- 프로젝트 명 : **CareBuddy** (케어버디)
- 프로젝트 정의 : 고령자 및 돌봄 대상자의 안전을 지키고 돌봄 부담을 완화하는 **레일 주행형 AI 모바일 로봇**
 <img width="650" height="300" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/carebuddy.jpg?raw=true" /></br>

**1-2. 개발 배경 및 필요성**
 1) 스마트 케어 시스템을 통해 효율적이고 지속 가능한 돌봄 환경 마련 필요

 2) 초고령화 사회 대응과 돌봄 인력 부족 해결 필요

 - 통계청의 ‘2024 고령자 통계’ 에 따르면, 2025년 65세 이상 고령 인구 전체 인구의 20% 이상 약 1,051만 명 예상
  - 요양보호사 수요 급증에도 불구하고, 2027년까지 약 7.5만 명 부족 예상
  - 현재 1명의 요양보호사가 5.3~8.8명의 대상자를 담당하는 등 과중한 업무 현실
    <img width="650" height="300" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/labor_shortage_projection.png?raw=true" /></br>

**1-3. 프로젝트 특장점**
- 기존 돌봄 장비 대비 실시간성과 정밀성이 향상된 스마트 시스템 
<img width="650" height="250" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/chart1.png?raw=true" /></br> 
- 기존 CCTV 기반 모니터링 대비 개선 효과
  
  <img width="650" height="300" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/chart2.png?raw=true" /></br>
 
**1-4. 주요 기능**
- **낙상 감지 AI 모델**: YOLOv8 object detection 기반으로 실시간 이상행동(낙상) 탐지
- **실시간 이동형 관측 시스템**: 레일형 로봇이 천장 구조를 따라 이동하여 사각지대 문제 해소
- **적외선(IR) 카메라 기반 야간 인식 기능**: 주.야간환경에서 24시간 실시간 감지 가능
- **모바일 실시간 알림 연동**: 이상행동 발생 시 보호자 앱으로 즉시 알림 전송
- **음성 인터페이스**: 이상행동 발생 시 블루투스 스피커를 통해 실내 경고 알림 제공


**1-5. 기대 효과 및 활용 분야**
1) 기대 효과 
- **즉각 대응**: 이상행동 실시간 감지 → 음성/앱 알림으로 보호자 및 의료진의 신속한 대응 가능
- **사각지대 최소화**: 이동형 레일 로봇 + IR 카메라로 주야간 감시 및 사각지대 해소
- **통행 방해 해소**: 천장 설치 구조로 바닥 공간 점유 없이 설치 가능.

2) 활용 분야 
- **의료·돌봄**: 요양병원, 요양원, 장애인 시설 등에서 낙상·실신 등 이상행동 실시간 감지 및 알림
- **보육시설**: 유아의 위험 행동·쓰러짐 등 시야 밖 상황 자동 인식
- **산업 현장**: 작업자의 이상 동작·재해 상황 조기 감지로 안전사고 예방
- **스마트 홈**: 1인 가구·고위험군의 돌발 행동 감지 및 비상 대응 지원


**1-6. 기술 스택**
- 프론트엔드 : React, Next.js, Tailwind CSS
- 백엔드 : Python(FastAPI), Node.js, Django
- AI/ML : PyTorch, TensorFlow, OpenAI API
- 데이터베이스 : PostgreSQL, MongoDB, Elasticsearch
- 배포 및 관리 : Docker, GitHub Actions

---

## **💡2. 팀원 소개**
| <img width="80" height="100" src="https://github.com/minseokim0207/assets/blob/master/img/mentee1.jpg?raw=true" > | <img width="80" height="100" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/mentee2.jpg?raw=true" > | <img width="80" height="100" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/mentee3.jpg?raw=true" > | <img width="80" height="100" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/mentee4.jpg?raw=true" > | 
|:---:|:---:|:---:|:---:|
| **김민서** | **박건희** | **라영웅** | **김효주** |
| • 개발총괄 <br> • 데이터 분석 | • UI/UX 기획 <br> • 영상편집 | • API 개발 <br> • DB 서버 구축 |• 데이터 분석 <br> • 전처리 | 



---
## **💡3. 시스템 구성도**
> **(참고)** S/W구성도, H/W구성도, 서비스 흐름도 등을 작성합니다. 시스템의 동작 과정 등을 추가할 수도 있습니다.
- 서비스 흐름도
  
<img width="650" height="300" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/ServiceFlowChart.png?raw=true" />

- S/W 구성도
  
<img width="650" height="550" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/SoftwareConfigurationDiagram.png?raw=true" />  

- H/W 구성도
  
<img width="650" height="600" alt="image" src="https://github.com/minseokim0207/assets/blob/master/img/hardware.png?raw=true" />  


<!-- 엔티티 관계도
  
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/76e3347b-6d94-491e-8aeb-a7b4601c54d5" /> -->


---
## **💡4. 작품 소개영상**
> **참고**: 썸네일과 유튜브 영상을 등록하는 방법입니다.
```Python
아래와 같이 작성하면, 썸네일과 링크등록을 할 수 있습니다.
[![영상 제목](유튜브 썸네일 URL)](유튜브 영상 URL)

작성 예시 : 저는 다음과 같이 작성하니, 아래와 같이 링크가 연결된 썸네일 이미지가 등록되었네요! 
[![한이음 드림업 프로젝트 소개](https://github.com/user-attachments/assets/16435f88-e7d3-4e45-a128-3d32648d2d84)](https://youtu.be/YcD3Lbn2FRI?si=isERqIAT9Aqvdqwp)
```
[![한이음 드림업 프로젝트 소개](https://github.com/minseokim0207/assets/blob/master/img/carebuddy_mockup.jpg?raw=true)](https://youtu.be/md-1Mj3nchI?si=9WYguuIe8CvcwUC6)


---
## **💡5. 핵심 소스코드**
- 소스코드 설명 : API를 활용해서 자동 배포를 생성하는 메서드입니다.

```Java
    private static void start_deployment(JsonObject jsonObject) {
        String user = jsonObject.get("user").getAsJsonObject().get("login").getAsString();
        Map<String, String> map = new HashMap<>();
        map.put("environment", "QA");
        map.put("deploy_user", user);
        Gson gson = new Gson();
        String payload = gson.toJson(map);

        try {
            GitHub gitHub = GitHubBuilder.fromEnvironment().build();
            GHRepository repository = gitHub.getRepository(
                    jsonObject.get("head").getAsJsonObject()
                            .get("repo").getAsJsonObject()
                            .get("full_name").getAsString());
            GHDeployment deployment =
                    new GHDeploymentBuilder(
                            repository,
                            jsonObject.get("head").getAsJsonObject().get("sha").getAsString()
                    ).description("Auto Deploy after merge").payload(payload).autoMerge(false).create();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
```
