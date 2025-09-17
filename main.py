from pedras import vence_puro, vence

print("Versão recursiva pura:")
for i in range(20):
    print(f"vence_puro({i}) = {vence_puro(i)}")

print("\nVersão com memorização:")
for i in range(20):
    print(f"vence({i}) = {vence(i)}")

print("\nTestando valor grande com memorização:")
print(f"vence(1000) = {vence(1000)}")