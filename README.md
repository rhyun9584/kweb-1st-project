# kweb-1st-project
Flask를 사용하여 만든 간단한 페이지

## 메인 페이지 (/)
로그인 페이지와 회원가입 페이지에 접근 가능

## 로그인 페이지 (/auth/signin/)
가입된 아이디와 비밀번호를 입력하여 로그인  
로그인 완료 시 회원 목록 페이지로 이동

## 회원가입 페이지 (/auth/signup/)
새로운 아이디를 생성  
회원가입 완료시 메인페이지로 이동

## 회원 목록 페이지 (/user/list/)
로그인된 유저의 아이디와 로그아웃 버튼으로 로그아웃 가능  
가입된 회원들의 목록 노출  
회원을 클릭하면 해당 회원의 프로필 페이지로 이동

## 회원 프로필 페이지 (/user/<user_id>)
회원의 이름, 아이디, 이메일, 생일 노출  
'Return to list' 버튼으로 회원 목록 페이지로 돌아감

## 로그아웃 기능 (/auth/signout/)
로그아웃하고 메인 페이지로 리다이렉트