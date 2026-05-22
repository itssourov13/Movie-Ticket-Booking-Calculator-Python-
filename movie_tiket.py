print("🎬 MOVIE TICKET BOOKING SYSTEM 🎬")
print("=" * 45)

# Basic info
base_price = 15
age = 21
seat_type = "Gold"
show_time = "Evening"

print(f"👤 Age: {age}")
print(f"💺 Seat Type: {seat_type}")
print(f"🕒 Show Time: {show_time}")
print("-" * 45)

# Eligibility check
if age > 17:
    print("✔ User is eligible to book a ticket")
else:
    print("❌ User is NOT eligible to book a ticket")

if age >= 21:
    print("✔ Eligible for Evening shows")
else:
    print("⚠ Not eligible for Evening shows")

print("-" * 45)

# Membership & discount
is_member = False
is_weekend = False
discount = 0

if is_member and age >= 21:
    discount = 3
    print("🎁 Membership discount applied: 3")
else:
    print("ℹ No membership discount")

print("💸 Discount:", discount)

print("-" * 45)

# Extra charges
extra_charges = 0

if is_weekend or show_time == "Evening":
    extra_charges = 2
    print("⚠ Extra charges applied: 2")
else:
    print("✔ No extra charges")

print("💰 Extra Charges:", extra_charges)

print("-" * 45)

# Final validation
if age >= 21 or (age >= 18 and (show_time != "Evening" or is_member)):

    print("🎟️ Booking condition satisfied")

    # Service charge based on seat
    if seat_type == "Premium":
        service_charges = 5
    elif seat_type == "Gold":
        service_charges = 3
    else:
        service_charges = 1

    print("🧾 Service Charges:", service_charges)

    # Final price calculation
    final_price = base_price + extra_charges + service_charges - discount

    print("-" * 45)
    print("💵 FINAL PRICE:", final_price)
    print("✅ Ticket booked successfully!")

else:
    print("❌ Ticket booking failed due to restrictions")

print("=" * 45)
print("🏁 END OF SYSTEM")

