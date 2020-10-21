import socket
import matplotlib.pyplot as plt

def decode_to_bin(msg):
	msg_bin = ""
	msg_aux = ""

	for elem in msg:
		msg_aux = bin(ord(elem))
		msg_aux = msg_aux[2:]
		if len(msg_aux) == 7:
			msg_aux = "0" + msg_aux
		msg_bin += msg_aux
		msg_aux = ""

	print("Mensagem em binário: " + msg_bin)
	return msg_bin

def print_B8ZS_server(msg):
	vetor = []
	vetor2 = []

	i = 1
	number_of_ones = 0
	number_of_zeros = 0
	for elem in msg:
		if int(elem) == 1 and number_of_ones % 2 == 0:
			vetor.append(int(elem))
			number_of_ones = number_of_ones + 1
			number_of_zeros = 0
		elif int(elem) == 1 and ((number_of_ones % 2) != 0):
			vetor.append(int(elem) * -1)
			number_of_ones = number_of_ones + 1
			number_of_zeros = 0
		else:
			number_of_zeros = number_of_zeros + 1
	
			if number_of_zeros == 8 and vetor[i - 9] == -1:
				vetor[i - 5] = -1
				vetor[i - 4] = 1
				vetor[i - 2] = 1
				vetor.append(-1)
				number_of_zeros = 0
				print("entrou")
			elif number_of_zeros == 8 and vetor[i - 9] == 1:
				vetor[i - 5] = 1
				vetor[i - 4] = -1
				vetor[i -2] = -1
				vetor.append(1)
				number_of_zeros = 0
				print("entrou")
			else:
				vetor.append(int(elem))

		vetor2.append(i)
		i = i + 1

	
	#print(len(vetor2))
	#print(len(vetor))
	plt.stem(vetor2,vetor)
	plt.show()

	msg = ""
	for elem in vetor:
		msg += str(elem)

	print("Mensagem aplicado o B8ZS: " + msg)
	return msg


msg = "o"
#print_B8ZS_server(decode_to_bin(msg))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s = setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((socket.gethostname(), 1234))
s.listen(5)

# now our endpoint knows about the OTHER endpoint.
clientsocket, address = s.accept()
#print(f"Connection from {address} has been established.")

msg = "çôõìíz"
print("Mensagem escrita: " + msg)
clientsocket.send(bytes(print_B8ZS_server(decode_to_bin(msg)), "utf-16"))


