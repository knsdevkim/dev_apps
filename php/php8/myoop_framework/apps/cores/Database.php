<?php
namespace apps\cores {
  use \PDO;

  class Database extends PDO {

    public function __construct() {
      if(!empty(DB_CONFIG['NAME'])) {
          parent::__construct(DB_CONFIG['ENGINE'] . ':host=' . DB_CONFIG['HOST'] . '; port=' . DB_CONFIG['PORT'] . '; dbname=' . DB_CONFIG['NAME'], DB_CONFIG['USER'], DB_CONFIG['PASSWORD']);
          parent::setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      } else { die('You are just using database without database name provided.'); }
    }

    public function select(string $table, ?array $fields, ?string $condition): array {
      $fields = (count($fields) <= 0) ? '*' : implode(', ', $fields);
      $prepare = 'SELECT ' . $fields . ' FROM ' . $table;
      $statement = ($condition == null) ? $prepare . ';' : $prepare . ' WHERE ' . $condition . ';';

      $sth = $this->prepare($statement);
      $sth->execute();
      $sth->setFetchMode(PDO::FETCH_ASSOC);
      return $sth->fetchAll();
    }

    protected function insert(string $table, array $fields): int {
      $prepare = 'INSERT INTO ' . $table . '(' . implode(', ', array_keys($fields)) . ') VALUES (' . '"' . implode('", "', array_values($fields)) .'"' . ');';
      $this->exec($prepare);
      return $this->lastInsertId();
    }

    protected function update(string $table, array $fields, ?string $condition): bool {
      $data = null;

      foreach($fields as $key => $value) {
        $data .= $key . '="' . $value . '", ';
      }
      $data = rtrim($data, ', ');
      $prepare = 'UPDATE ' . $table . ' SET ' . $data . ' WHERE ' . $condition . ';';

      return $this->exec($prepare);
    }

    protected function delete(string $table, string $condition): bool {
      $prepare = 'DELETE FROM ' . $table . ' WHERE ' . $condition . ';';
      return $this->exec($prepare);
    }

    protected function queue($prepare): array {
      $sth = $this->prepare($prepare);
      $sth->execute();
      $sth->setFetchMode(PDO::FETCH_ASSOC);
      return $sth->fetchAll();
    }
  }
}
