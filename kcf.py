# 1. 필요한 라이브러리 가져오기-openCV 라이브러리
import cv2

# 2. KCF 추적기 만들기
tracker = cv2.TrackerKCF.create()

# 3. 비디오 파일 열기
video = cv2.VideoCapture('race.mp4')
ok, frame = video.read()


# 4. ROI-관심영역 선택
bbox = cv2.selectROI(frame)

# 5. 선택한 ROI로 트래커 초기화
ok = tracker.init(frame, bbox)

# 6. 객체를 추적하기 위해 각 프레임을 반복
while True:
    ok, frame = video.read()
    if not ok:
        break
# 7. 추적기 업데이트
    ok, bbox = tracker.update(frame)
    
# 8. 추적 결과 그리기
    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2, 1)
    else:
        cv2.putText(frame, 'Error', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
# 9. 프레임 표시
    cv2.imshow('Tracking', frame)

# 10. 키를 누를 때 루프 종료
    if cv2.waitKey(1) & 0XFF == 27: # ESC
        break
# 11. 클린업
    # video.release()
    # cv2.destroyAllWindows()
    


