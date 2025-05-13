
import requests
import os

def download_aas_file(aas_file_id, save_path):
    # API 엔드포인트 URL
    url = f'http://localhost:3000/api/aas-files/download/{aas_file_id}'
    
    # GET 요청 보내기
    response = requests.get(url, stream=True)
    
    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # 파일명 가져오기 (응답 헤더에서)
        filename = response.headers.get('content-disposition', '').split('filename=')[-1].strip('"')
        if not filename:
            filename = f'aas_file_{aas_file_id}.aasx'
        
        # 파일 저장 경로 생성
        file_path = os.path.join(save_path, filename)
        
        # 파일 저장하기
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f'파일 다운로드 완료: {file_path}')
        return file_path
    else:
        print(f'다운로드 실패: 상태 코드 {response.status_code}')
        print(response.text)
        return None

# 사용 예시
if __name__ == '__main__':
    aas_file_id = 2  # 다운로드할 파일의 ID
    save_directory = './downloads'  # 파일 저장 경로
    
    # 저장 디렉토리가 없으면 생성
    os.makedirs(save_directory, exist_ok=True)
    
    # 파일 다운로드
    downloaded_file = download_aas_file(aas_file_id, save_directory)


