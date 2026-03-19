import subprocess
import os

def check_with_k_framework(old_phase, new_phase):
    """
    This function writes a small K program, runs it via 'krun',
    and checks if the result is SAFE.
    """
    # 1. Write the command to a temporary file (e.g., check(NS_GREEN, NS_YELLOW))
    # This creates the file that K Framework will read
    k_code = f"check({old_phase}, {new_phase})"
    
    with open("temp_request.k", "w") as f:
        f.write(k_code)
        
    try:
        # 2. Run krun
        # --term ensures we get the clean result
        # This is the command that executes formal verification
        output = subprocess.check_output(
            ["krun", "temp_request.k"], 
            stderr=subprocess.STDOUT
        ).decode("utf-8")
        
        # 3. Check if K Framework responded with <k> SAFE </k>
        # The K output looks something like this: <k> SAFE </k>
        if "SAFE" in output:
            return True
        else:
            # If K returns something else (e.g., gets stuck), it means UNSAFE
            print(f"[K-FRAMEWORK] REJECTED! Transaction {old_phase} -> {new_phase} is not Safe.")
            return False
            
    except Exception as e:
        print(f"Error executing K: {e}")
        return False

def ensure_safe_transition(func):
    """
    The decorator that protects the traffic light change function.
    """
    def wrapper(intersection, new_phase):
        old_phase = intersection.current_phase
        
        # --- VERIFICATION TAKES PLACE HERE ---
        print(f"📡 [K-Framework] Verifying the transaction: {old_phase} -> {new_phase}...")
        
        is_safe = check_with_k_framework(old_phase, new_phase)
        
        if is_safe:
            # If K says YES, we execute the switch
            print("✅ [K-Framework] SAFE. Execute the switch.")
            return func(intersection, new_phase)
        else:
            # If K says NO, we block everything. The traffic light will not change.
            print("⛔ [K-Framework] UNSAFE! Transaction blocked.")
            return None

    return wrapper