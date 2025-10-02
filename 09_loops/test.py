memberships = {
    "Basic": 500,
    "Premium": 1500,
    "VIP": 3000
}

print(f"iBall Membership Calculator")
print("-" * 30)

for tier, monthly_price in memberships.items():
    annual = monthly_price * 12
    discount = annual * 0.10
    annual_with_discount = annual - discount

    print(f"{tier} Membership:")
    print(f" Montly: KSH {monthly_price:,}")
    print(f" Annual: KSH {annual:,}")
    print(f" Annual(10% off): KSH {annual_with_discount:,.0f}")
    print()