import random


class Computer:
    def __init__(self, id, ip):
        self.id = id
        self.ip = ip
        self.buffer = None

    def __repr__(self):
        return f"C{self.id}({self.ip}) -> {self.buffer if self.buffer else 'null'}"


class Token:
    def __init__(self):
        self.source_ip = None
        self.dest_ip = None
        self.message = None
        self.busy = False
        self.delivered = False

    def reset(self):
        self.dest_ip = None
        self.message = None
        self.busy = False
        self.delivered = False


def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def initialize_network():
    return [Computer(i, generate_random_ip()) for i in range(10)]


def select_source_dest(network):
    return random.sample(network, 2)


def print_network_state(network):
    for computer in network:
        print(computer)
    print()


def token_ring_simulation():
    network = initialize_network()
    token = Token()
    previous_src = network[0]

    messages = ["Salut!", "Test mesaj", "Token Ring Simulare", "Hello, world!", "Python Networking"]

    for step in range(10):
        print(f"=== Pasul {step + 1} ===")
        print_network_state(network)

        src, dest = select_source_dest(network)
        message = random.choice(messages)

        print(f"Sursa: C{src.id} Destinatia: C{dest.id}")

        token.source_ip = src.ip
        token.dest_ip = dest.ip
        token.message = message
        token.busy = True
        token.delivered = False

        current_index = previous_src.id

        while current_index != src.id:
            print(f"C{network[current_index].id}: Muta jetonul către noua sursă")
            current_index = (current_index + 1) % len(network)

        while token.busy:
            print(f"C{network[current_index].id}: Muta jetonul")

            if network[current_index].ip == dest.ip:
                print(f"C{network[current_index].id}: Am ajuns la destinatie")
                network[current_index].buffer = token.message
                token.delivered = True
                break

            current_index = (current_index + 1) % len(network)

        while token.delivered:
            print(f"C{network[current_index].id}: Muta jetonul")

            if network[current_index].ip == src.ip:
                print(f"C{network[current_index].id}: Am ajuns inapoi")
                token.reset()
                break

            current_index = (current_index + 1) % len(network)

        previous_src = src

        print_network_state(network)


if __name__ == "__main__":
    token_ring_simulation()