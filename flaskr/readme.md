# Term Project #4

Address Book by Web

**web_server.py를 실행하여 서버 가동**

*© 서유림, 이정훈*



## Environment

- Framework
  - Flask
- 사용한 언어
  - Python
  - Javascript
  - JQuery
  - HTML
  - CSS
- Database
  - SQLite3




## Features

### Contacts 연락처

1. Add

   새로운 연락처를 추가합니다. 이름, 전화번호, 이메일을 입력 받아 DB에 저장합니다.

   전화번호를 key 값으로 사용하여 이미 있는 전화번호는 추가할 수 없습니다. 이름과 이메일은 중복을 허용합니다.

2. Search

   하나의 검색창에서 이름, 전화번호, 이메일 통합검색 기능을 제공합니다.

   부분 검색 기능을 지원합니다.

3. Call

   Call 버튼을 눌러 전화를 겁니다.

   발신 기록은 현재 시각을 반영하여 임의로 통화 시간 20초로 기록됩니다.

4. Send Message

   Message 버튼을 눌러 SMS를 전송합니다.

   발신 기록은 현재 시각을 반영하여 기록되며, 사용자가 원하는 내용을 입력하여 메시지를 전송할 수 있습니다.

5. Edit

   기존 연락처를 수정합니다.

6. Delete

   연락처를 삭제합니다.



### Call History 통화기록

1. Show

   전화번호가 DB에 저장되어 있는 경우 번호 대신 이름을 보여줍니다.

   - All

     DB에 있는 모든 통화 기록을 보여줍니다.

     통화 시간의 단위는 초(s)입니다.

   - Sent Calls

     발신 전화 목록을 보여줍니다.

   - Received Calls

     수신 전화 목록을 보여줍니다.

   - Missed Calls

     부재중 전화 목록을 보여줍니다.



### Message Box 문자기록

1. Show

   전화번호가 DB에 저장되어 있는 경우 번호 대신 이름을 보여줍니다.

   - All Messages

     DB에 있는 모든 메시지를 보여줍니다.

   - Sent Messages

     보낸 메시지를 보여줍니다.

   - Received Messages

     받은 메시지를 보여줍니다.



## Database

- SQLite3
- Filename : addressbook.db
- DB Name : ADDRESSBOOK
- Table & Column Name
  - ADDRESSBOOK
    - id - INTEGER, primary key, autoincrement
    - name - TEXT
    - number - TEXT
    - email - TEXT
  - CALL
    - time - TEXT
    - phone - TEXT
    - status - INTEGER (0: SENT, 1: RECEIVED, 2: MISSED)
    - duration - TEXT
  - SMS
    - time - TEXT
    - phone - TEXT
    - status - INTEGER (0: SENT, 1: RECEIVED, 2: MISSED)
    - content - TEXT



## GitHub

[GitHub OODP Term Project 4](https://github.com/sur801/oodp_term4)

