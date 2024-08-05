import json
import os
from datetime import datetime, timedelta

# Caminho para o arquivo de dados
DATA_FILE = 'agenda.json'


def load_data():
    """Carrega os compromissos do arquivo de dados, se existir."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_data(data):
    """Salva os compromissos no arquivo de dados."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def add_event(agenda):
    """Adiciona um novo evento à agenda."""
    title = input("Digite o título do evento: ").strip()
    date_str = input("Digite a data e hora do evento (YYYY-MM-DD HH:MM): ").strip()
    reminder_minutes = input(
        "Digite o número de minutos antes para o lembrete (ou deixe em branco para nenhum): ").strip()

    try:
        event_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        reminder = int(reminder_minutes) if reminder_minutes else None
        reminder_time = event_date - timedelta(minutes=reminder) if reminder else None

        agenda[title] = {
            'date': event_date.isoformat(),
            'reminder': reminder_time.isoformat() if reminder_time else None
        }

        print(f"Evento '{title}' adicionado com sucesso.")
    except ValueError:
        print("Data e hora inválidas. Certifique-se de seguir o formato 'YYYY-MM-DD HH:MM'.")


def view_agenda(agenda):
    """Exibe a agenda com os eventos e lembretes."""
    if not agenda:
        print("A agenda está vazia.")
        return

    for title, details in agenda.items():
        event_date = datetime.fromisoformat(details['date'])
        reminder_time = datetime.fromisoformat(details['reminder']) if details['reminder'] else None
        reminder_info = f"Lembrete: {reminder_time.strftime('%Y-%m-%d %H:%M')}" if reminder_time else "Sem lembrete"

        print(f"Título: {title}")
        print(f"Data e Hora: {event_date.strftime('%Y-%m-%d %H:%M')}")
        print(reminder_info)
        print("-" * 40)


def main():
    agenda = load_data()

    while True:
        print("\nMenu:")
        print("1. Adicionar evento")
        print("2. Ver agenda")
        print("3. Sair")

        choice = input("Escolha uma opção: ").strip()

        if choice == '1':
            add_event(agenda)
        elif choice == '2':
            view_agenda(agenda)
        elif choice == '3':
            save_data(agenda)
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
