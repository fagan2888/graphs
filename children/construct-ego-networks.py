import argparse
import collections

def main():
  parser = argparse.ArgumentParser(description='Generate bi-ego networks. Writes files that are named node1-node2.edges')
  parser.add_argument('-o', required=True,  dest='output_folder', help='output folder')
  parser.add_argument('-e', required=True, dest='edges', help='edge file')
  parser.add_argument('-n', required=True, dest='nodes', help='node attribute file')
  args = parser.parse_args()
  node_gender = {}
  for line in open(args.nodes):
    node, gender = line.split()[0], line.strip().split()[2]
    if gender == 'M' or gender == 'F':
      node_gender[node] = gender
  neighbors = collections.defaultdict(lambda: set())
  for line in open(args.edges):
    node1, node2 = line.strip().split()
    neighbors[node1].add(node2)      
    neighbors[node2].add(node1)      
  statistics = open('corpus-statistics', 'w')
  for node1 in neighbors:
    if node1 in node_gender:
      output = open('%s/%s-%s.edges' % (args.output_folder, node1, node1), 'w')
      all_nodes = neighbors[node1].union(neighbors[node1])
      for node in all_nodes:
        for neb in neighbors[node]:
          if neb in all_nodes:
            output.write('%s %s\n' % (node, neb))
      output.close()
    
if __name__ == '__main__':
  main()
