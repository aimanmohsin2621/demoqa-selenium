from PIL import Image, ImageChops, ImageStat

def compare_images(img1_path, img2_path, tolerance=10):
    """
    Compare two images and return True if they're visually similar.
    Tolerance = how much difference (0–100) we allow before failing.
    """
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    # Resize to same size (in case one image is slightly different)
    if img1.size != img2.size:
        img2 = img2.resize(img1.size)

    diff = ImageChops.difference(img1, img2)
    stat = ImageStat.Stat(diff)
    mean_diff = sum(stat.mean) / len(stat.mean)

    if mean_diff < tolerance:
        print(f"✅ Images match closely! (diff={mean_diff:.2f})")
        return True
    else:
        print(f"⚠️ Images differ too much (diff={mean_diff:.2f})")
        diff.save("artifacts/difference.png")  # save visual diff for debugging
        return False


