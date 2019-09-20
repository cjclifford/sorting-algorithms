import sys, time, random
import socket
import visualizer, sort

algorithms = [
  'bubble',
  'insertion',
  'selection',
  # 'merge',
  'heap',
  'shell',
  'comb',
  'cocktail',
  'quick'
]

def main():
  args = [arg.lower() for arg in sys.argv[1:]]
  if args[0] == '--server':
    if len(args) != 2 or not args[1].isdigit():
      print_usage()
      return
    host = socket.gethostname()
    port = 8080

    s = socket.socket()
    s.bind((host, port))

    clients = []

    for _ in range(int(args[1])):
      s.listen(1)
      client_socket, address = s.accept()
      clients.append({'socket': client_socket, 'address': address})
      print(f'connection from {str(address)}')

    message = ''
    while message != 's' and message != 'q':
      message = input('[s]tart/[q]uit? > ')

    if message == 's':
      for client in clients:
        client['socket'].send('start'.encode('utf-8'))

    for client in clients:
      client['socket'].close()

    s.close()
  elif args[0] == '--client':
    if len(args) != 2:
      print_usage()
      return
    host = socket.gethostname()
    port = 8080

    s = socket.socket()
    s.connect((host, port))

    lst, vis = init_visualizer()

    message = ''
    while message != 'start' and message != 'quit':
      message = s.recv(1024).decode('utf-8')

    if message == 'start':
      run_visualizer(lst, vis, args)

    s.close()
  elif args[0] == '--algorithm':
    if len(args) != 2:
      print_usage()
      return
    lst, vis = init_visualizer()
    run_visualizer(lst, vis, args)
  else:
    print_usage()


def init_visualizer():
  vis = visualizer.Visualizer(500, 500)

  lst = [i for i in range(100)]
  random.shuffle(lst)

  return lst, vis

def run_visualizer(lst, vis, args):
  if 'bubble' in args:
    visualize_bubble_sort(lst[:], vis)
  elif 'insertion' in args:
    visualize_insertion_sort(lst[:], vis)
  elif 'selection' in args:
    visualize_selection_sort(lst[:], vis)
  elif 'heap' in args:
    visualize_heap_sort(lst[:], vis)
  elif 'shell' in args:
    visualize_shell_sort(lst[:], vis)
  elif 'comb' in args:
    visualize_comb_sort(lst[:], vis)
  elif 'cocktail' in args:
    visualize_cocktail_shaker_sort(lst[:], vis)
  elif 'quick' in args:
    visualize_quick_sort(lst[:], vis)
  # TODO: merge sort visualization
  else:
    print('Not a valid algorithm')
    print(f"Valid algorithms: [{', '.join(algorithms)}]")

def visualize_bubble_sort(lst, vis):
  start_time = time.perf_counter_ns()
  sort.bubble_sort(lst, vis)
  end_time = time.perf_counter_ns()

  vis.replay()
  vis.reset()

  print('Bubble Sort')
  print(f'Time: {end_time - start_time:,}ns\n')

def visualize_insertion_sort(lst, vis):
  start_time = time.perf_counter_ns()
  sort.insertion_sort(lst, vis)
  end_time = time.perf_counter_ns()

  vis.replay()
  vis.reset()

  print('Insertion Sort')
  print(f'Time: {end_time - start_time:,}ns\n')

def visualize_selection_sort(lst, vis):
  start_time = time.perf_counter_ns()
  sort.selection_sort(lst, vis)
  end_time = time.perf_counter_ns()

  vis.replay(0)
  vis.reset()

  print('Selection Sort')
  print(f'Time: {end_time - start_time:,}ns\n')

def visualize_heap_sort(lst, vis):
  start_time = time.perf_counter_ns()
  sort.heap_sort(lst, vis)
  end_time = time.perf_counter_ns()

  vis.replay(0)
  vis.reset()

  print('Heap Sort')
  print(f'Time: {end_time - start_time:,}ns\n')

def visualize_shell_sort(lst, vis):
  gaps = [10, 5, 3, 2, 1]

  start_time = time.perf_counter_ns()
  sort.shell_sort(lst, gaps, vis)
  end_time = time.perf_counter_ns()

  vis.replay(0)
  vis.reset()

  print('Shell Sort')
  print(f'Time: {end_time - start_time:,}ns\n')

def visualize_comb_sort(lst, vis):
  start_time = time.perf_counter_ns()
  sort.comb_sort(lst, 1.3, vis)
  end_time = time.perf_counter_ns()

  vis.replay(0)
  vis.reset()

  print('Comb Sort')
  print(f'Time: {end_time - start_time:,}ns\n')

def visualize_cocktail_shaker_sort(lst, vis):
  start_time = time.perf_counter_ns()
  sort.cocktail_shaker_sort(lst, vis)
  end_time = time.perf_counter_ns()

  vis.replay(0)
  vis.reset()

  print('Cocktail Shaker Sort')
  print(f'Time: {end_time - start_time:,}ns\n')

def visualize_quick_sort(lst, vis):
  start_time = time.perf_counter_ns()
  sort.quick_sort(lst, 0, len(lst) - 1, vis)
  end_time = time.perf_counter_ns()

  vis.replay(0)
  vis.reset()

  print('Quick Sort')
  print(f'Time: {end_time - start_time:,}ns\n')

def print_usage():
  print('Usage: python main.py [[--server number_of_clients] | [--client algorithm] | [--algorithm algorithm]]')

if __name__ == '__main__':
  main()