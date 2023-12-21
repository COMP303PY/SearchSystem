import requests

def game_info(game_name, extension="System Requirements"):
    url = "http://127.0.0.1:5000/games"
    gpu_url = "http://127.0.0.1:5000/GPU"
    cpu_url = "http://127.0.0.1:5000/CPU"

    try:
        response = requests.get(url)
        data = response.json()

        for game in data:
            if game_name.lower() in game["name"].lower():
                graphics_card = space_control(game.get("Graphics Card:", ""), " or")
                cpu = space_control(game.get("CPU:", ""), " or").lstrip()  # Başındaki boşlukları temizle
                file_size = game.get("File Size:", "")
                memory = game.get("Memory:", "")
                os_version = game.get("OS:", "")


                gpu_model = getrank(graphics_card, gpu_url)
                rank_gpu = f"RankGPU: {gpu_model}" if gpu_model != "N/A" else ""


                cpu_model = getrank(cpu, cpu_url)
                rank_cpu = f"RankCPU: {cpu_model}" if cpu_model != "N/A" else ""


                game_requirements = f"{game['name']} {extension}"

                print(f"Game: {game_requirements}")
                print(f"Graphics Card: {graphics_card} ({rank_gpu})")
                print(f"CPU: {cpu} ({rank_cpu})")
                print(f"File Size: {file_size}")
                print(f"Memory: {memory}")
                print(f"OS: {os_version}")
                print(f"Url: {graphics_card}+{cpu}")
                break
        else:
            print(f"Game '{game_name}' not found in the database.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def space_control(text, keyword):
    index = text.lower().find(keyword.lower())
    if index != -1:
        return text[:index].strip()
    else:
        return text

def getrank(model, component_url):
    try:
        response = requests.get(component_url)
        data = response.json()

        for component in data:
            if model.lower() in component["Model"].lower():
                return component["Rank"]
        else:
            return "N/A"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {component_url}: {e}")
        return "N/A"

# Kullanım örneği
game_name = "Fortnite"
game_info(game_name)
