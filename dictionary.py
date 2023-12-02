day=input("Türkçe gün adı:")
TrEn={'pazartesi':"monday", "salı":"tuesday", "çarşamba":"wednesday","perşembe":"Thursday", "cuma":"friday","cumartesi":"saturday","spazar":"sunday"}
print("ingilizcesi:",end=" ")
print(TrEn.get(day,"bu kelime sözlükte yok!"))
