create table company (
    company_no bigint not null AUTO_INCREMENT  primary key,
    company_name varchar(255) not null,
    company_location varchar(255) not null
);

INSERT INTO company (company_name, company_location) VALUES
('알파 코퍼레이션', '서울특별시 강남구 테헤란로 123, 강남타워 5층'),
('베타 산업', '서울특별시 종로구 청계천로 456, 종로빌딩 10층'),
('감마 주식회사', '대구광역시 중구 동성로 789, 동성로센터 3층'),
('델타 엔터프라이즈', '대구광역시 수성구 범어로 101, 범어빌딩 7층'),
('입실론 주식회사', '인천광역시 연수구 송도문화로 202, 송도파크 8층'),
('제타 솔루션즈', '인천광역시 부평구 부평대로 303, 부평플라자 6층'),
('에타 시스템즈', '광주광역시 서구 무진대로 404, 무진빌딩 9층'),
('세타 테크놀로지스', '광주광역시 북구 중흥로 505, 중흥타워 4층'),
('아이오타 그룹', '전주전라북도 전주시 완산구 전주천동로 606, 전주사무소 11층'),
('카파 홀딩스', '전주전라북도 완주군 이서면 전북대로 707, 이서타운 2층'),
('람다 코퍼레이션', '목포전라남도 목포시 상동 808, 상동센터 5층'),
('뮤 엔터프라이즈', '순천전라남도 순천시 조례동 909, 조례빌딩 3층'),
('누 주식회사', '춘천강원도 춘천시 중앙로 1010, 춘천타워 7층'),
('크사이 시스템즈', '원주강원도 원주시 강원로 1111, 원주센터 4층'),
('오미크론 주식회사', '서울특별시 동작구 사당로 1212, 사당빌딩 8층'),
('파이 솔루션즈', '서울특별시 송파구 올림픽로 1313, 올림픽타워 6층'),
('로우 테크놀로지스', '대구광역시 달서구 달구벌대로 1414, 달서센터 2층'),
('시그마 홀딩스', '대구광역시 동구 동대구로 1515, 동대구빌딩 9층'),
('타우 그룹', '광주광역시 남구 봉선로 1616, 봉선타워 5층'),
('입실론 코퍼레이션', '광주광역시 동구 동명로 1717, 동명센터 3층'),
('알파베타 코퍼레이션', '서울특별시 강남구 삼성로 123, 삼성타워 5층'),
('베타감마 산업', '서울특별시 종로구 관철동 456, 관철빌딩 10층'),
('감마델타 주식회사', '대구광역시 중구 대구로 789, 대구타워 3층'),
('델타입실론 엔터프라이즈', '대구광역시 수성구 수성로 101, 수성타워 7층'),
('입실론제타 주식회사', '인천광역시 연수구 송도지하도 202, 송도센터 8층'),
('제타에타 솔루션즈', '인천광역시 부평구 부평역로 303, 부평타워 6층'),
('에타세타 시스템즈', '광주광역시 서구 화정로 404, 화정센터 9층'),
('세타아이오타 테크놀로지스', '광주광역시 북구 금남로 505, 금남타워 4층'),
('아이오타카파 그룹', '전주전라북도 전주시 혁신로 606, 혁신타워 11층'),
('카파람다 홀딩스', '전주전라북도 완주군 삼례로 707, 삼례센터 2층'),
('람다뮤 코퍼레이션', '목포전라남도 목포시 해안로 808, 해안타워 5층'),
('뮤누 엔터프라이즈', '순천전라남도 순천시 왕조로 909, 왕조센터 3층'),
('누크사이 주식회사', '춘천강원도 춘천시 동면로 1010, 동면타워 7층'),
('크사이오미크론 시스템즈', '원주강원도 원주시 산업로 1111, 산업센터 4층'),
('오미크론파이 주식회사', '서울특별시 동작구 노량진로 1212, 노량진타워 8층'),
('파이로우 솔루션즈', '서울특별시 송파구 잠실로 1313, 잠실타워 6층'),
('로우타우 테크놀로지스', '대구광역시 달서구 월배로 1414, 월배센터 2층'),
('타우입실론 홀딩스', '대구광역시 동구 아양로 1515, 아양타워 9층'),
('입실론피 그룹', '광주광역시 남구 진월로 1616, 진월센터 5층'),
('피카이 엔터프라이즈', '광주광역시 동구 금동로 1717, 금동타워 3층'),
('카이베타 주식회사', '서울특별시 강남구 테헤란로 1234, 강남타워 5층'),
('프사이델타 엔터프라이즈', '서울특별시 종로구 명륜로 1234, 명륜센터 10층'),
('델타입실론 주식회사', '대구광역시 중구 중앙로 1234, 중앙센터 3층'),
('입실론제타 엔터프라이즈', '대구광역시 수성구 상동로 1234, 상동타워 7층'),
('제타에타 주식회사', '인천광역시 연수구 송도로 1234, 송도타워 8층'),
('에타세타 솔루션즈', '인천광역시 부평구 부평로 1234, 부평센터 6층'),
('세타아이오타 시스템즈', '광주광역시 서구 화정로 1234, 화정타워 9층'),
('아이오타카파 테크놀로지스', '광주광역시 북구 금남로 1234, 금남센터 4층'),
('카파람다 그룹', '전주전라북도 전주시 전주로 1234, 전주센터 11층'),
('람다뮤 홀딩스', '전주전라북도 완주군 삼례로 1234, 삼례타워 2층'),
('뮤누 주식회사', '목포전라남도 목포시 해안로 1234, 해안센터 5층'),
('누크사이 엔터프라이즈', '순천전라남도 순천시 왕조로 1234, 왕조센터 3층'),
('크사이오미크론 시스템즈', '춘천강원도 춘천시 동면로 1234, 동면센터 7층'),
('오미크론파이 주식회사', '원주강원도 원주시 산업로 1234, 산업타워 4층'),
('파이로우 테크놀로지스', '서울특별시 동작구 노량진로 1234, 노량진센터 8층'),
('로우타우 솔루션즈', '서울특별시 송파구 잠실로 1234, 잠실센터 6층'),
('타우입실론 주식회사', '대구광역시 달서구 월배로 1234, 월배타워 2층'),
('입실론피 엔터프라이즈', '대구광역시 동구 아양로 1234, 아양센터 9층'),
('피카이 시스템즈', '광주광역시 남구 진월로 1234, 진월타워 5층'),
('카이베타 주식회사', '광주광역시 동구 금동로 1234, 금동센터 3층'),
('프사이델타 홀딩스', '서울특별시 강남구 테헤란로 1234, 강남센터 6층'),
('델타입실론 엔터프라이즈', '서울특별시 종로구 명륜로 1234, 명륜타워 10층'),
('입실론제타 주식회사', '대구광역시 중구 중앙로 1234, 중앙타워 3층'),
('제타에타 솔루션즈', '대구광역시 수성구 상동로 1234, 상동센터 7층'),
('에타세타 시스템즈', '인천광역시 연수구 송도로 1234, 송도센터 8층'),
('세타아이오타 주식회사', '인천광역시 부평구 부평로 1234, 부평타워 6층'),
('아이오타카파 테크놀로지스', '광주광역시 서구 치평로 1234, 치평타워 9층'),
('카파람다 그룹', '광주광역시 북구 운암로 1234, 운암센터 4층'),
('람다뮤 홀딩스', '전주전라북도 전주시 전주로 1234, 전주타워 11층'),
('뮤누 주식회사', '전주전라북도 완주군 삼례로 1234, 삼례센터 2층'),
('누크사이 엔터프라이즈', '목포전라남도 목포시 해안로 1234, 해안타워 5층'),
('크사이오미크론 시스템즈', '순천전라남도 순천시 왕조로 1234, 왕조타워 3층'),
('오미크론파이 주식회사', '춘천강원도 춘천시 동면로 1234, 동면타워 7층'),
('파이로우 테크놀로지스', '원주강원도 원주시 산업로 1234, 산업센터 4층'),
('로우타우 솔루션즈', '서울특별시 동작구 노량진로 1234, 노량진센터 8층'),
('타우입실론 주식회사', '서울특별시 송파구 잠실로 1234, 잠실타워 6층'),
('입실론피 엔터프라이즈', '대구광역시 달서구 월배로 1234, 월배센터 2층'),
('피카이 시스템즈', '대구광역시 동구 아양로 1234, 아양타워 9층'),
('카이베타 주식회사', '광주광역시 남구 진월로 1234, 진월센터 5층'),
('프사이델타 홀딩스', '광주광역시 동구 금동로 1234, 금동타워 3층');


create table department (
    depmt_no bigint not null AUTO_INCREMENT primary key,
    company_no bigint(255) not null,
    depmt_name varchar(255) not null,
    landline varchar(255),
    location varchar(255) not null,
    CONSTRAINT FK_depmt_company_no FOREIGN KEY (company_no) REFERENCES company(company_no)
);

-- 회사 1
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(1, '인사팀', '02-1234-5678', '서울특별시 강남구 테헤란로 123, 강남타워 3층 301호'),
(1, '재무팀', '02-2345-6789', '서울특별시 강남구 테헤란로 123, 강남타워 3층 302호');

-- 회사 2
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(2, '마케팅팀', '02-3456-7890', '서울특별시 종로구 청계천로 456, 종로빌딩 4층 401호'),
(2, '영업팀', '02-4567-8901', '서울특별시 종로구 청계천로 456, 종로빌딩 4층 402호');

-- 회사 3
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(3, '개발팀', '053-1234-5678', '대구광역시 중구 동성로 789, 동성로센터 6층 601호'),
(3, '지원팀', '053-2345-6789', '대구광역시 중구 동성로 789, 동성로센터 6층 602호');

-- 회사 4
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(4, '연구팀', '053-3456-7890', '대구광역시 수성구 범어로 101, 범어빌딩 7층 701호'),
(4, '운영팀', '053-4567-8901', '대구광역시 수성구 범어로 101, 범어빌딩 7층 702호');

-- 회사 5
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(5, '디자인팀', '032-1234-5678', '인천광역시 연수구 송도문화로 202, 송도파크 8층 801호'),
(5, '콘텐츠팀', '032-2345-6789', '인천광역시 연수구 송도문화로 202, 송도파크 8층 802호');

-- 회사 6
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(6, '기획팀', '032-3456-7890', '인천광역시 부평구 부평대로 303, 부평플라자 2층 201호'),
(6, '서비스팀', '032-4567-8901', '인천광역시 부평구 부평대로 303, 부평플라자 2층 202호');

-- 회사 7
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(7, 'HR팀', '062-1234-5678', '광주광역시 서구 무진대로 404, 무진빌딩 9층 901호'),
(7, 'IT팀', '062-2345-6789', '광주광역시 서구 무진대로 404, 무진빌딩 9층 902호');

-- 회사 8
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(8, '법무팀', '062-3456-7890', '광주광역시 북구 중흥로 505, 중흥타워 10층 1001호'),
(8, '경영팀', '062-4567-8901', '광주광역시 북구 중흥로 505, 중흥타워 10층 1002호');

-- 회사 9
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(9, '운영팀', '063-1234-5678', '전주전라북도 전주시 완산구 전주천동로 606, 전주사무소 4층 401호'),
(9, '지원팀', '063-2345-6789', '전주전라북도 전주시 완산구 전주천동로 606, 전주사무소 4층 402호');

-- 회사 10
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(10, '기획팀', '063-3456-7890', '전주전라북도 완주군 이서면 전북대로 707, 이서타운 6층 601호'),
(10, '마케팅팀', '063-4567-8901', '전주전라북도 완주군 이서면 전북대로 707, 이서타운 6층 602호');


-- 회사 11
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(11, '인사팀', '02-5678-1234', '서울특별시 강서구 공항대로 212, 강서타워 2층 203호'),
(11, '재무팀', '02-6789-2345', '서울특별시 강서구 공항대로 212, 강서타워 2층 204호');

-- 회사 12
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(12, '마케팅팀', '02-7890-3456', '서울특별시 마포구 월드컵로 333, 마포빌딩 6층 601호'),
(12, '영업팀', '02-8901-4567', '서울특별시 마포구 월드컵로 333, 마포빌딩 6층 602호');

-- 회사 13
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(13, '개발팀', '053-5678-1234', '대구광역시 북구 유통단지로 444, 유통센터 3층 303호'),
(13, '지원팀', '053-6789-2345', '대구광역시 북구 유통단지로 444, 유통센터 3층 304호');

-- 회사 14
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(14, '연구팀', '053-7890-3456', '대구광역시 중구 중앙대로 555, 중앙타워 5층 505호'),
(14, '운영팀', '053-8901-4567', '대구광역시 중구 중앙대로 555, 중앙타워 5층 506호');

-- 회사 15
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(15, '디자인팀', '032-5678-1234', '인천광역시 남동구 예술로 666, 예술타워 4층 401호'),
(15, '콘텐츠팀', '032-6789-2345', '인천광역시 남동구 예술로 666, 예술타워 4층 402호');

-- 회사 16
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(16, '기획팀', '032-7890-3456', '인천광역시 서구 원적로 777, 원적빌딩 7층 701호'),
(16, '서비스팀', '032-8901-4567', '인천광역시 서구 원적로 777, 원적빌딩 7층 702호');

-- 회사 17
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(17, 'HR팀', '062-5678-1234', '광주광역시 동구 금남로 888, 금남타워 8층 801호'),
(17, 'IT팀', '062-6789-2345', '광주광역시 동구 금남로 888, 금남타워 8층 802호');

-- 회사 18
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(18, '법무팀', '062-7890-3456', '광주광역시 남구 서문로 999, 서문빌딩 9층 901호'),
(18, '경영팀', '062-8901-4567', '광주광역시 남구 서문로 999, 서문빌딩 9층 902호');

-- 회사 19
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(19, '운영팀', '063-5678-1234', '전주전라북도 완산구 전주천로 1010, 전주타워 6층 601호'),
(19, '지원팀', '063-6789-2345', '전주전라북도 완산구 전주천로 1010, 전주타워 6층 602호');

-- 회사 20
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(20, '기획팀', '063-7890-3456', '전주전라북도 덕진구 중앙로 2020, 중앙타워 8층 801호'),
(20, '마케팅팀', '063-8901-4567', '전주전라북도 덕진구 중앙로 2020, 중앙타워 8층 802호');

-- 회사 21
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(21, 'HR팀', '02-9012-3456', '서울특별시 동대문구 청량리로 111, 청량리타워 3층 303호'),
(21, 'IT팀', '02-0123-4567', '서울특별시 동대문구 청량리로 111, 청량리타워 3층 304호');

-- 회사 22
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(22, '법무팀', '02-1234-5678', '서울특별시 성동구 왕십리로 222, 왕십리타워 4층 401호'),
(22, '경영팀', '02-2345-6789', '서울특별시 성동구 왕십리로 222, 왕십리타워 4층 402호');

-- 회사 23
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(23, '연구팀', '053-9012-3456', '대구광역시 동구 중앙로 333, 중앙타워 6층 601호'),
(23, '운영팀', '053-0123-4567', '대구광역시 동구 중앙로 333, 중앙타워 6층 602호');

-- 회사 24
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(24, '디자인팀', '053-1234-5678', '대구광역시 서구 팔공로 444, 팔공빌딩 5층 505호'),
(24, '콘텐츠팀', '053-2345-6789', '대구광역시 서구 팔공로 444, 팔공빌딩 5층 506호');

-- 회사 25
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(25, '기획팀', '032-9012-3456', '인천광역시 부평구 부평대로 555, 부평빌딩 7층 701호'),
(25, '서비스팀', '032-0123-4567', '인천광역시 부평구 부평대로 555, 부평빌딩 7층 702호');

-- 회사 26
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(26, 'HR팀', '032-1234-5678', '인천광역시 연수구 송도문화로 666, 송도타워 8층 801호'),
(26, 'IT팀', '032-2345-6789', '인천광역시 연수구 송도문화로 666, 송도타워 8층 802호');

-- 회사 27
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(27, '법무팀', '062-9012-3456', '광주광역시 서구 화정로 777, 화정타워 5층 501호'),
(27, '경영팀', '062-0123-4567', '광주광역시 서구 화정로 777, 화정타워 5층 502호');

-- 회사 28
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(28, '연구팀', '062-1234-5678', '광주광역시 남구 봉선로 888, 봉선타워 6층 601호'),
(28, '운영팀', '062-2345-6789', '광주광역시 남구 봉선로 888, 봉선타워 6층 602호');

-- 회사 29
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(29, '디자인팀', '063-9012-3456', '전주전라북도 덕진구 전주로 999, 전주타워 5층 501호'),
(29, '콘텐츠팀', '063-0123-4567', '전주전라북도 덕진구 전주로 999, 전주타워 5층 502호');

-- 회사 30
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(30, '기획팀', '063-1234-5678', '전주전라북도 완산구 전주천로 1010, 전주타워 4층 401호'),
(30, '서비스팀', '063-2345-6789', '전주전라북도 완산구 전주천로 1010, 전주타워 4층 402호');

-- 회사 31
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(31, 'HR팀', '02-3456-7890', '서울특별시 강북구 삼각산로 111, 삼각산타워 2층 203호'),
(31, 'IT팀', '02-4567-8901', '서울특별시 강북구 삼각산로 111, 삼각산타워 2층 204호');

-- 회사 32
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(32, '법무팀', '02-5678-9012', '서울특별시 관악구 관악로 222, 관악빌딩 3층 301호'),
(32, '경영팀', '02-6789-0123', '서울특별시 관악구 관악로 222, 관악빌딩 3층 302호');

-- 회사 33
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(33, '연구팀', '053-3456-7890', '대구광역시 달서구 상인로 333, 상인타워 4층 401호'),
(33, '운영팀', '053-4567-8901', '대구광역시 달서구 상인로 333, 상인타워 4층 402호');

-- 회사 34
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(34, '디자인팀', '053-5678-9012', '대구광역시 수성구 범어로 444, 범어빌딩 6층 601호'),
(34, '콘텐츠팀', '053-6789-0123', '대구광역시 수성구 범어로 444, 범어빌딩 6층 602호');

-- 회사 35
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(35, '기획팀', '032-3456-7890', '인천광역시 남동구 논현로 555, 논현타워 5층 501호'),
(35, '서비스팀', '032-4567-8901', '인천광역시 남동구 논현로 555, 논현타워 5층 502호');

-- 회사 36
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(36, 'HR팀', '032-5678-9012', '인천광역시 연수구 송도대로 666, 송도타워 6층 601호'),
(36, 'IT팀', '032-6789-0123', '인천광역시 연수구 송도대로 666, 송도타워 6층 602호');

-- 회사 37
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(37, '법무팀', '062-3456-7890', '광주광역시 북구 서암로 777, 서암타워 4층 401호'),
(37, '경영팀', '062-4567-8901', '광주광역시 북구 서암로 777, 서암타워 4층 402호');

-- 회사 38
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(38, '연구팀', '062-5678-9012', '광주광역시 동구 충장로 888, 충장타워 6층 601호'),
(38, '운영팀', '062-6789-0123', '광주광역시 동구 충장로 888, 충장타워 6층 602호');

-- 회사 39
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(39, '디자인팀', '063-3456-7890', '전주전라북도 덕진구 전주로 999, 덕진타워 5층 501호'),
(39, '콘텐츠팀', '063-4567-8901', '전주전라북도 덕진구 전주로 999, 덕진타워 5층 502호');

-- 회사 40
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(40, '기획팀', '063-5678-9012', '전주전라북도 완산구 전주천로 1010, 완산타워 4층 401호'),
(40, '서비스팀', '063-6789-0123', '전주전라북도 완산구 전주천로 1010, 완산타워 4층 402호');

-- 회사 41
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(41, 'HR팀', '02-7890-1234', '서울특별시 강서구 공항대로 123, 공항타워 2층 203호'),
(41, 'IT팀', '02-8901-2345', '서울특별시 강서구 공항대로 123, 공항타워 2층 204호');

-- 회사 42
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(42, '법무팀', '02-9012-3456', '서울특별시 마포구 월드컵로 234, 월드컵타워 3층 301호'),
(42, '경영팀', '02-0123-4567', '서울특별시 마포구 월드컵로 234, 월드컵타워 3층 302호');

-- 회사 43
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(43, '연구팀', '053-7890-1234', '대구광역시 북구 유통단지로 345, 유통타워 4층 401호'),
(43, '운영팀', '053-8901-2345', '대구광역시 북구 유통단지로 345, 유통타워 4층 402호');

-- 회사 44
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(44, '디자인팀', '053-9012-3456', '대구광역시 수성구 범어로 456, 범어타워 6층 601호'),
(44, '콘텐츠팀', '053-0123-4567', '대구광역시 수성구 범어로 456, 범어타워 6층 602호');

-- 회사 45
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(45, '기획팀', '032-7890-1234', '인천광역시 남동구 논현로 567, 논현타워 5층 501호'),
(45, '서비스팀', '032-8901-2345', '인천광역시 남동구 논현로 567, 논현타워 5층 502호');

-- 회사 46
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(46, 'HR팀', '032-9012-3456', '인천광역시 연수구 송도대로 678, 송도타워 6층 601호'),
(46, 'IT팀', '032-0123-4567', '인천광역시 연수구 송도대로 678, 송도타워 6층 602호');

-- 회사 47
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(47, '법무팀', '062-7890-1234', '광주광역시 서구 화정로 789, 화정타워 5층 501호'),
(47, '경영팀', '062-8901-2345', '광주광역시 서구 화정로 789, 화정타워 5층 502호');

-- 회사 48
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(48, '연구팀', '062-9012-3456', '광주광역시 동구 충장로 890, 충장타워 6층 601호'),
(48, '운영팀', '062-0123-4567', '광주광역시 동구 충장로 890, 충장타워 6층 602호');

-- 회사 49
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(49, '디자인팀', '063-7890-1234', '전주전라북도 덕진구 전주로 1011, 덕진타워 5층 501호'),
(49, '콘텐츠팀', '063-8901-2345', '전주전라북도 덕진구 전주로 1011, 덕진타워 5층 502호');

-- 회사 50
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(50, '기획팀', '063-9012-3456', '전주전라북도 완산구 전주천로 1111, 완산타워 4층 401호'),
(50, '서비스팀', '063-0123-4567', '전주전라북도 완산구 전주천로 1111, 완산타워 4층 402호');

-- 회사 51
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(51, 'HR팀', '02-2345-6789', '서울특별시 강북구 삼각산로 123, 삼각산타워 2층 203호'),
(51, 'IT팀', '02-3456-7890', '서울특별시 강북구 삼각산로 123, 삼각산타워 2층 204호');

-- 회사 52
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(52, '법무팀', '02-4567-8901', '서울특별시 관악구 관악로 234, 관악빌딩 3층 301호'),
(52, '경영팀', '02-5678-9012', '서울특별시 관악구 관악로 234, 관악빌딩 3층 302호');

-- 회사 53
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(53, '연구팀', '053-2345-6789', '대구광역시 달서구 상인로 345, 상인타워 4층 401호'),
(53, '운영팀', '053-3456-7890', '대구광역시 달서구 상인로 345, 상인타워 4층 402호');

-- 회사 54
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(54, '디자인팀', '053-4567-8901', '대구광역시 수성구 범어로 456, 범어타워 6층 601호'),
(54, '콘텐츠팀', '053-5678-9012', '대구광역시 수성구 범어로 456, 범어타워 6층 602호');

-- 회사 55
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(55, '기획팀', '032-2345-6789', '인천광역시 남동구 논현로 567, 논현타워 5층 501호'),
(55, '서비스팀', '032-3456-7890', '인천광역시 남동구 논현로 567, 논현타워 5층 502호');

-- 회사 56
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(56, 'HR팀', '032-4567-8901', '인천광역시 연수구 송도대로 678, 송도타워 6층 601호'),
(56, 'IT팀', '032-5678-9012', '인천광역시 연수구 송도대로 678, 송도타워 6층 602호');

-- 회사 57
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(57, '법무팀', '062-2345-6789', '광주광역시 북구 서암로 789, 서암타워 4층 401호'),
(57, '경영팀', '062-3456-7890', '광주광역시 북구 서암로 789, 서암타워 4층 402호');

-- 회사 58
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(58, '연구팀', '062-4567-8901', '광주광역시 동구 충장로 890, 충장타워 6층 601호'),
(58, '운영팀', '062-5678-9012', '광주광역시 동구 충장로 890, 충장타워 6층 602호');

-- 회사 59
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(59, '디자인팀', '063-2345-6789', '전주전라북도 덕진구 전주로 1011, 덕진타워 5층 501호'),
(59, '콘텐츠팀', '063-3456-7890', '전주전라북도 덕진구 전주로 1011, 덕진타워 5층 502호');

-- 회사 60
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(60, '기획팀', '063-4567-8901', '전주전라북도 완산구 전주천로 1111, 완산타워 4층 401호'),
(60, '서비스팀', '063-5678-9012', '전주전라북도 완산구 전주천로 1111, 완산타워 4층 402호');

-- 회사 61
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(61, 'HR팀', '02-5678-1234', '서울특별시 강북구 삼각산로 131, 삼각산타워 3층 303호'),
(61, 'IT팀', '02-6789-2345', '서울특별시 강북구 삼각산로 131, 삼각산타워 3층 304호');

-- 회사 62
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(62, '법무팀', '02-7890-3456', '서울특별시 관악구 관악로 245, 관악빌딩 4층 401호'),
(62, '경영팀', '02-8901-4567', '서울특별시 관악구 관악로 245, 관악빌딩 4층 402호');

-- 회사 63
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(63, '연구팀', '053-5678-1234', '대구광역시 달서구 상인로 357, 상인타워 5층 501호'),
(63, '운영팀', '053-6789-2345', '대구광역시 달서구 상인로 357, 상인타워 5층 502호');

-- 회사 64
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(64, '디자인팀', '053-7890-3456', '대구광역시 수성구 범어로 468, 범어타워 6층 601호'),
(64, '콘텐츠팀', '053-8901-4567', '대구광역시 수성구 범어로 468, 범어타워 6층 602호');

-- 회사 65
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(65, '기획팀', '032-5678-1234', '인천광역시 남동구 논현로 678, 논현타워 6층 601호'),
(65, '서비스팀', '032-6789-2345', '인천광역시 남동구 논현로 678, 논현타워 6층 602호');

-- 회사 66
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(66, 'HR팀', '032-7890-3456', '인천광역시 연수구 송도대로 789, 송도타워 7층 701호'),
(66, 'IT팀', '032-8901-4567', '인천광역시 연수구 송도대로 789, 송도타워 7층 702호');

-- 회사 67
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(67, '법무팀', '062-6789-1234', '광주광역시 서구 화정로 890, 화정타워 6층 601호'),
(67, '경영팀', '062-7890-2345', '광주광역시 서구 화정로 890, 화정타워 6층 602호');

-- 회사 68
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(68, '연구팀', '062-8901-3456', '광주광역시 동구 충장로 901, 충장타워 7층 701호'),
(68, '운영팀', '062-9012-4567', '광주광역시 동구 충장로 901, 충장타워 7층 702호');

-- 회사 69
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(69, '디자인팀', '063-6789-1234', '전주전라북도 덕진구 전주로 1022, 덕진타워 5층 501호'),
(69, '콘텐츠팀', '063-7890-2345', '전주전라북도 덕진구 전주로 1022, 덕진타워 5층 502호');

-- 회사 70
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(70, '기획팀', '063-8901-3456', '전주전라북도 완산구 전주천로 1122, 완산타워 4층 401호'),
(70, '서비스팀', '063-9012-4567', '전주전라북도 완산구 전주천로 1122, 완산타워 4층 402호');


-- 회사 71
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(71, '기획팀', '02-1234-5678', '서울특별시 종로구 종로 123, 종로타워 3층 301호'),
(71, '서비스팀', '02-2345-6789', '서울특별시 종로구 종로 123, 종로타워 3층 302호');

-- 회사 72
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(72, 'HR팀', '02-3456-7890', '서울특별시 강남구 테헤란로 456, 강남타워 6층 601호'),
(72, 'IT팀', '02-4567-8901', '서울특별시 강남구 테헤란로 456, 강남타워 6층 602호');

-- 회사 73
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(73, '법무팀', '053-5678-9012', '대구광역시 동구 동대구로 789, 동대구타워 4층 401호'),
(73, '경영팀', '053-6789-0123', '대구광역시 동구 동대구로 789, 동대구타워 4층 402호');

-- 회사 74
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(74, '연구팀', '053-7890-1234', '대구광역시 서구 서대구로 890, 서대구타워 5층 501호'),
(74, '운영팀', '053-8901-2345', '대구광역시 서구 서대구로 890, 서대구타워 5층 502호');

-- 회사 75
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(75, '디자인팀', '032-1234-5678', '인천광역시 미추홀구 미추홀로 234, 미추홀타워 7층 701호'),
(75, '콘텐츠팀', '032-2345-6789', '인천광역시 미추홀구 미추홀로 234, 미추홀타워 7층 702호');

-- 회사 76
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(76, '기획팀', '032-3456-7890', '인천광역시 부평구 부평로 345, 부평타워 5층 501호'),
(76, '서비스팀', '032-4567-8901', '인천광역시 부평구 부평로 345, 부평타워 5층 502호');

-- 회사 77
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(77, 'HR팀', '062-5678-9012', '광주광역시 서구 상무대로 456, 상무타워 6층 601호'),
(77, 'IT팀', '062-6789-0123', '광주광역시 서구 상무대로 456, 상무타워 6층 602호');

-- 회사 78
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(78, '법무팀', '062-7890-1234', '광주광역시 북구 용봉로 567, 용봉타워 7층 701호'),
(78, '경영팀', '062-8901-2345', '광주광역시 북구 용봉로 567, 용봉타워 7층 702호');

-- 회사 79
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(79, '해외팀', '053-6789-0123', '대구광역시 동구 동대구로 1515, 동대구빌딩 4층 401호'),
(79, '물류팀', '053-7890-1234', '대구광역시 동구 동대구로 1515, 동대구빌딩 4층 402호');

-- 회사 80
INSERT INTO department (company_no, depmt_name, landline, location) VALUES
(80, '재무팀', '062-6789-0123', '광주광역시 남구 봉선로 1616, 봉선타워 7층 701호'),
(80, '인사팀', '062-7890-1234', '광주광역시 남구 봉선로 1616, 봉선타워 7층 702호');




CREATE TABLE employee (
    emp_no BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    depmt_no BIGINT NOT NULL,
    company_no BIGINT NOT NULL,
    name VARCHAR(255) NOT NULL,
    phone_no VARCHAR(255) NOT NULL,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 갱신 시간
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- 생성 시간
    CONSTRAINT FK_emp_depmt_no FOREIGN KEY (depmt_no) REFERENCES department(depmt_no),
    CONSTRAINT FK_emp_company_no FOREIGN KEY (company_no) REFERENCES company(company_no)
);

create table source (
    emp_no BIGINT not null,
    gateway VARCHAR(255) NOT NULL,
    ip_address VARCHAR(255) NOT NULL,
    mac_address VARCHAR(255) NOT NULL,
    PRIMARY KEY (emp_no),
    CONSTRAINT FK_source_emp_no FOREIGN KEY (emp_no) REFERENCES employee(emp_no) ON DELETE CASCADE
);

create table users (
    emp_no bigint not null,
    email varchar(255) not null,
    depmt_no bigint not null,
    company_no bigint not null,
    password varchar(255) not null,
    user_role int not null default 0,
    PRIMARY KEY (email, emp_no),
    CONSTRAINT FK_user_emp_no FOREIGN KEY (emp_no) REFERENCES employee(emp_no) ON DELETE CASCADE
);


create table refresh_token (
    token_no bigint not null AUTO_INCREMENT PRIMARY KEY,
    email varchar(255) not null,
    depmt_no bigint not null,
    company_no bigint not null,
    CONSTRAINT FK_token_email FOREIGN KEY (email) REFERENCES users(email),
    CONSTRAINT FK_token_depmt_no FOREIGN KEY (depmt_no) REFERENCES department(depmt_no),
    CONSTRAINT FK_token_company_no FOREIGN KEY (company_no) REFERENCES company(company_no)
);



