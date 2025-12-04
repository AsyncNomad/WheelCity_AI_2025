## 1. 솔루션 한 줄 요약 (One-line Summary)

**일상 속 접근성 정보를 AI로 자동 판별하여 제공하는 사용자 참여형 배리어프리맵**

**A crowdsourced barrier-free map that automatically identifies accessibility information using AI.**

## 2. 풀고자 하는 사회 문제 정의 (Problem Definition)

### **"정보의 부재가 물리적 장애만큼 큰 장벽입니다."**

### **"Absence of information is as big a barrier as physical disability."**

- **접근성 정보 확인의 어려움**: 휠체어 사용자의 70%가 목적지에 경사로 등이 있는지 확인하는 데 어려움을 겪고 있습니다.
- **정보의 부재**: 지도나 리뷰 플랫폼에 등록된 장소 중 60%는 접근 가능 여부에 대한 정보조차 없습니다.
- **기존 서비스의 한계**:
    - **지속성 부족**: 초기 데이터 구축 후 업데이트가 되지 않아 정보의 신뢰도가 낮습니다.
    - **데이터 파편화**: 정보가 여러 곳에 흩어져 있어 통합적인 확인이 어렵습니다.
    - **지역 편중**: 서울 및 수도권에 데이터가 집중되어 있습니다.
- **Difficulty in checking accessibility**: 70% of wheelchair users find it difficult to check if a destination has ramps or stairs.
- **Absence of Information**: 60% of places on maps or review platforms lack even basic accessibility information.
- **Limitations of Existing Services**:
    - **Lack of Sustainability**: Information reliability drops due to a lack of updates after initial data construction.
    - **Data Fragmentation**: Information is scattered, making integrated verification difficult.
    - **Regional Bias**: Data is concentrated in Seoul and metropolitan areas.

## 3. 솔루션 개요 (Solution Overview)

### **휠도시의 핵심 기능 (Key Features)**

1. **간편한 데이터 수집 (Simple Data Collection)**: 사용자 참여(Crowdsourcing)를 통해 장소와 이미지 입력을 최대한 간단하게 만듭니다.
2. **AI 기반 자동 판별 (AI-based Automatic Detection)**: **YOLOv8**과 **Gemini**를 활용한 2-step 모델로 입구 사진만으로 접근성 정보(경사로 유무, 문턱 등)를 표준화된 태그로 자동 생성합니다.
3. **신뢰도 강화 루프 (Reliability Loop)**: 지도 시각화 및 사용자 피드백을 통해 데이터가 지속적으로 업데이트되고 정교해지는 선순환 구조를 만듭니다.

### **기대 효과 및 차별점 (Expected Effects & Differentiation)**

- **지속적인 최신화**: 관리 미흡으로 방치되는 기존 지도와 달리, 사용자 참여와 AI 자동화를 통해 정보를 최신 상태로 유지합니다.
- **방대한 데이터 커버리지**: 자동화된 검증을 통해 특정 지역에 국한되지 않고 일반 지도 서비스 수준의 넓은 커버리지를 목표로 합니다.
- **개인 맞춤형 정보**: 사용자의 휠체어 스펙을 고려하여 개인별 접근 가능 여부를 제공합니다.

### **Differentiation**

- **Continuous Updates**: Unlike existing static maps, we maintain up-to-date information through user participation and AI automation.
- **Massive Data Coverage**: We aim for broad coverage comparable to general map services through automated verification.
- **Personalized Information**: We provide accessibility details tailored to individual wheelchair specifications.

## 4. 설치 및 실행 방법 (Installation & Usage)

이 프로젝트는 Frontend와 Backend 리포지토리로 구성되어 있습니다. 상세한 설치 및 실행 방법은 각 리포지토리를 참고해 주세요.
This project consists of Frontend and Backend repositories. Please refer to each repository for detailed installation and execution instructions.

### **Frontend (HTML / Javascript / CSS)**

- **Repository**: https://github.com/lollipop719/WheelCity_front_2025

```
git clone https://github.com/lollipop719/WheelCity_front_2025
cd WheelCity_front_2025
npm install
npm start

```

### **Backend (Python / FastAPI)**

- **Repository**: https://github.com/kang022878/WheelCity_back_2025
- **AI Models**: YOLOv8, Gemini API
- **Database**: MongoDB, AWS S3

```
git clone https://github.com/kang022878/wheel_city_server
cd wheel_city_server
pip install -r requirements.txt
uvicorn main:app --reload

```

### **AI (YOLOv8, Gemini API)**

- **Repository**: https://github.com/AsyncNomad/WheelCity_AI_2025

## 5. 데모 영상 (Demo Video)

https://drive.google.com/file/d/1FDLIXpQlXcAVRUNkvkp9R28v2NBAAoga/view?usp=sharing

## 6. 연관 자료 (References)

- **협동조합 무의 (Cooperative Muui)**: [프로젝트 협력 파트너 (Project Partner)](https://www.wearemuui.com/)
- **관련 기술 (Tech Stack)**: YOLOv8, Gemini API, React Native, FastAPI, MongoDB

## 7. 팀 및 팀원 소개 (Team Introduction)

- **Team 휠도시 (WheelCity)**는 KAIST CS499 <테크 포 임팩트> 수업의 일환으로, 기술을 통해 이동약자의 정보 불평등 문제를 해결하고자 합니다.

### **Members**

- **고은서 (Ko Eunseo)**: PM (Project Manager)
- **권정준 (Gwon Jeongjoon)**: UI/UX, Front-end Developer
- **이상범 (Lee Sangbum)**: AI Engineer, Front-end Developer
- **황지훈 (Hwang Jihoon)**: Full Stack Developer
- **강서현 (Kang Seohyun)**: Back-end Developer

### **Partners**

- **협동조합 무의 (Cooperative Muui)**: 멘토링 및 필드 데이터 지원 (Mentoring & Field Data Support)
- **카카오 멘토 김성민 (Kakao Mentor Kris):** 기술 멘토링

### **Contact (Github / Email)**

- 고은서: @esgogo02 / esgogo@kaist.ac.kr
- 권정준: @gwonjeongjoon / jgwon7436@kaist.ac.kr
- 이상범: @AsyncNomad / sangddung2@kaist.ac.kr
- 황지훈: @lollipop719 / jihwang@kaist.ac.kr
- 강서현: @kang022878 / kang022878@kaist.ac.kr

---

# 건물 입구 휠체어 접근성 분석 AI - Wheel City AI 2

`Wheel City AI 2`는 건물 입구 이미지 한 장으로 휠체어 접근성을 자동으로 분석하고 판단하는 딥러닝 기반 프로젝트입니다. **YOLOv8**의 객체 탐지 기술과 **Gemini**의 상황 인지 능력을 결합하여, 사진 속 장소에 대해 이동 약자의 통행 가능 여부를 판단합니다.

## 프로젝트 메커니즘

이 프로젝트는 두 가지 AI 모델이 유기적으로 협력하는 파이프라인 구조로 동작합니다.

1. **1단계: 객체 탐지 (YOLOv8m)**
    - 사용자가 `test_images` 폴더에 이미지를 입력하면, 사전 학습된 **YOLOv8m 모델**이 먼저 작동합니다.
    - 모델은 이미지 내에서 휠체어 접근성의 핵심 요소인 턱/계단(curb)과 경사로(ramp)를 탐지합니다.
    - 탐지된 객체에는 바운딩 박스(Bounding Box)가 표시되며, 이 시각화된 이미지는 Gemini에 input으로 전달됩니다.
2. **2단계: 종합 판단 (Gemini 2.5 Flash / Gemini 2.5 Pro)**
    - 1단계에서 생성된 바운딩 박스 이미지를 **Gemini**가 입력받습니다.
    - Gemini는 단순 객체 유무를 넘어, "턱이 있지만, 문으로 이어지는 유효한 경사로가 있는가?"와 같이 **이미지의 전체적인 맥락과 상황을 종합적으로 이해**하고 추론합니다.
    - 최종적으로, Gemini는 접근성 규칙에 기반하여 `accessible` (접근 가능 여부), `reason` (판단 이유)이 포함된 구조화된 **JSON 형식의 최종 결과**를 생성합니다.

---

## 사용 모델 (Models Used)

| 역할 | 모델 이름 | 상세 정보 |
| --- | --- | --- |
| **객체 탐지** | YOLOv8 | Ultralytics의 작고 빠른 객체 탐지 모델로 로컬에서 동작 |
| **종합 판단** | Gemini 2.5 Flash / Pro | Google AI Studio를 통해 API 호출로 동작 |

---

## 디렉토리 구조

```bash
wheel_city_ai/
├── yolov8/                   # YOLOv8 모델을 위한 프로젝트 폴더
│   ├── prepare_dataset.py    # 모델 학습에 필요한 이미지, xml 데이터를 input 형식에 맞게 변환
│   ├── train.py              # YOLOv8을 학습시키기 위한 스크립트
│   ├── run.py                # step 2. YOLOv8 분석을 실행하는 스크립트
│   └── ...                   # (학습 데이터, 모델 가중치 등)
│
├── gemini/                   # gemini 모델을 위한 프로젝트 폴더
│   ├── run.py                # step 3. gemini 분석을 실행하는 스크립트
│   └── ...                   
├── runner/                   # 전체 과정 실행 프로그램을 위한 프로젝트 폴더
│   ├── main.rs               # 전체 과정을 자동화한 최종 실행 프로그램 코드
│   └── ...                   # (모델 가중치 등)
│
├── input_images/           # step 1. 입력할 사진을 넣는 디렉토리
│── bbox_images/            # YOLO의 분석 결과 사진이 임시 저장되는 디렉토리
└── results/                # 결과 json 파일이 저장되는 디렉토리
```

---

## 사용 방법
YOLOv8은 YOLOv8m 모델로 학습해놓은 샘플 ver14가 yolov8/train_result/에 있습니다. 학습을 통해 커스텀할 것이 아니라면 그대로 사용해도 됩니다.
### 1. Runner를 이용하는 손쉬운 사용 방법
이미지를 드래그하거나 불러온 뒤 Run 버튼을 누르면 결과를 보여주는 runner 프로그램을 사용할 수 있습니다.
아래 명령어를 입력하여 runner를 실행합니다.

```bash
cd runner
cargo run
```

1. **이미지 입력:**
- 이미지를 드래그하거나 선택합니다. 여러 장의 이미지도 가능합니다.
 <img src="https://github.com/user-attachments/assets/94a09910-e3fe-400d-920d-9aa64dbc88ec" width="1000" height="600"/>

2. **Run 버튼을 눌러 실행, 결과 확인**
- 최종 분석 결과는 `results/` 폴더 안의 `result.json` 파일에서 확인할 수 있습니다.
 <img src="https://github.com/user-attachments/assets/01d84243-ae6e-4086-84da-abdd9fe8c934" width="1000" height="500"/>

### 2. 스크립트 실행으로 사용하는 방법
1. **이미지 입력:**
    - `test_images/` 폴더에 분석하고 싶은 건물 입구 이미지를 넣습니다.
2. **YOLOv8 실행 (객체 탐지):**
    - `yolov8` 폴더로 이동하여 `run.py` 스크립트를 실행합니다.
    - 실행이 완료되면 `bbox_images/` 폴더에 바운딩 박스가 표시된 이미지들이 생성됩니다.
3. **Gemini 실행 (최종 판단):**
    - `gemini/` 폴더로 이동하여 `run.py` 스크립트를 실행합니다.
4. **결과 확인:**
    - 최종 분석 결과는 `results/` 폴더 안의 `result.json` 파일에서 확인할 수 있습니다.

---

## 실행 예시

1. **이미지 입력**

 <img src="https://github.com/user-attachments/assets/58d210dc-d75a-4fa5-b0d0-7a3e4660ed41" width="400" height="600"/>

2. **YOLOv8m이 output 생성, gemini에 텍스트 프롬프트와 함께 입력**

 <img src="https://github.com/user-attachments/assets/7922035e-7c24-4dc0-8d1d-39ef42a27135" width="400" height="600"/>

```python
SYSTEM_PROMPT = (
    "You are an accessibility analysis AI. Analyze the provided image of a building entrance to determine if it is accessible for a lone wheelchair user.\n"
    "Accessibility Rules:\n"
    "1. There must be no steps or curbs between the ground and the entrance.\n"
    "2. If there are steps or curbs, a ramp must connect the ground to the entrance.\n\n"
    "Return ONLY valid JSON. Do not include any explanations, Markdown, or code fences.\n"
    'JSON schema: {"accessible": boolean | null, "reason": string}\n'
)
```

3. **Gemini가 상황을 종합적으로 판단하여 최종 의사결정, 스크립트를 통해 JSON으로 파싱**

```json
{
  "results": [
    {
      "image": "annotated_data1.jpg",
      "result": {
        "accessible": true,
        "reason": "The building entrance has a permanent ramp connecting the ground to the entrance, making it accessible for a lone wheelchair user despite the presence of curbs."
      }
    }
  ]
}
```

---

## 🛠️ 환경 설정 (Ubuntu 24.04 기준)
실행 전 .env 반드시 수정하기. 본인의 API KEY 설정 필수.
```bash
# Google Gemini
GOOGLE_API_KEY="여기 자신의 API KEY 넣기"

# 사용할 YOLO 모델 (n, s, m, l, x 중 선택)
YOLO_MODEL=yolov8m.pt

# 데이터셋 yaml
YOLO_DATA=yolov8/data_balanced.yaml

# 학습 설정
EPOCHS=50
IMGSZ=640
BATCH=8

# 결과 저장 폴더 이름
RUN_NAME=ver1
```
