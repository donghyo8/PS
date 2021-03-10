def solution(phone_book):
    answer = True
    phone_book.sort()

    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            answer = False
            break

    return answer

phone_book1 = ["119", "97674223", "1195524421"]
phone_book2 = ["123","456","789"]
phone_book3 = ["12","123","1235","567","88"]
solution(phone_book3)