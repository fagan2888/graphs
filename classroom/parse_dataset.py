import argparse

def main():
  parser = argparse.ArgumentParser(description='Generate a graph and a node attribute file from gexf file')
  parser.add_argument('-i', required=True,  dest='input', help='Input attribute file. \'individual_attr.txt\'')
  parser.add_argument('-f', required=True,  dest='friendship', help='Input friendship file. \'individual_edges_friend_sem2.txt\'')
  parser.add_argument('-e', required=True, dest='edges', help='Output edge file')
  parser.add_argument('-n', required=True, dest='nodes', help='Output node attribute file')
  args = parser.parse_args()
  attrb_file = open(args.input)
  attrb_file.readline()
  node_file = open(args.nodes, 'w')
  edge_file = open(args.edges, 'w')
  for line in attrb_file:
    node_id, gender = line.split()[:2]
    if gender == '1':
      gender = 'M'
    if gender == '2':
      gender = 'F'
    node_file.write('%s dummy %s\n' % (node_id, gender))
  node_file.close()

  friend_file = open(args.friendship)
  friend_file.readline()
  edges = set()
  for line in friend_file:
    try:
      source, target = sorted(line.split()[:2])
    except:
      print 'ERROR'
      print line
      quit()
    if source+'_'+target not in edges:
      edge_file.write('%s %s\n' % (source, target))
      edges.add(source + '_'+target)
  edge_file.close()
if __name__ == '__main__':
  main()
