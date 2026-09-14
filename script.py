import time

def start_game():
    print("=" * 60)
    print("🌌 Space Survival Adventure | مغامرة النجاة في الفضاء 🌌")
    print("=" * 60)
    print("Your spaceship crashed on a mysterious planet...")
    print("سقطت مركبتك الفضائية اضطرارياً على كوكب غامض...")
    print("\nChoose your path / اختر طريقك:")
    print("1. Enter the dark alien forest / دخول الغابة الفضائية المظلمة")
    print("2. Climb the high dangerous mountain / صعود الجبل العالي الخطير")
    
    choice = input("Enter your choice (1 or 2) / اختر رقم الطريق: ")
    
    if choice == "1":
        forest_path()
    elif choice == "2":
        mountain_path()
    else:
        print("Invalid choice! Restart the game. / اختيار غير صحيح! أعد تشغيل اللعبة.")

def forest_path():
    print("\n🌲 You entered the dark forest... / لقد دخلت إلى الغابة المظلمة...")
    print("You found an old glowing box next to a sleeping alien creature.")
    print("وجدت صندوقاً قديماً يلمع بجانب مخلوق فضائي نائم.")
    print("\nWhat will you do? / ماذا تفعل؟")
    print("1. Open the box quietly / تفتح الصندوق بهدوء")
    print("2. Run back quickly / تهرب بسرعة للوراء")
    
    choice = input("Enter your choice (1 or 2) / اختر رقم التصرف: ")
    if choice == "1":
        print("\n🎉 Congratulations! You found the energy core and escaped safely!")
        print("🎉 مبروك! وجدت نواة الطاقة ونجحت في الهرب بسلام!")
    else:
        print("\n💀 Bad luck! The creature woke up and caught you. Game Over!")
        print("💀 للأسف! استيقظ المخلوق وأمسك بك. انتهت اللعبة!")

def mountain_path():
    print("\n⛰️ You climbed to the top of the mountain... / صعدت إلى قمة الجبل...")
    print("You found an abandoned base locked with a digital code.")
    print("وجدت قاعدة مهجورة مغلقة بكلمة سر رقمية.")
    print("\nWhat will you do? / ماذا تفعل؟")
    print("1. Guess the code (1234) / تخمين الكلمة (1234)")
    print("2. Search for another way around / البحث عن طريق آخر")
    
    choice = input("Enter your choice (1 or 2) / اختر رقم التصرف: ")
    if choice == "1":
        print("\n🎉 Success! The door opened, you found a new ship. You Win!")
        print("🎉 نجحت! انفتح الباب ووجدت سفينة جديدة. أنت الفائز!")
    else:
        print("\n❄️ You slipped in the cold darkness. Game Over!")
        print("❄️ انزلقت في الظلام والبرد القارص. انتهت اللعبة!")

if __name__ == "__main__":
    start_game()
