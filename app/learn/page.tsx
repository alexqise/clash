import Link from "next/link"
import Image from "next/image"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { ChevronRight, BookOpen, Trophy } from "lucide-react"

export default function LearnPage() {
  const winConditions = [
    { id: "hog-rider", name: "Hog Rider", type: "Building Targeter", elixir: 4 },
    { id: "royal-giant", name: "Royal Giant", type: "Building Targeter", elixir: 6 },
    { id: "golem", name: "Golem", type: "Tank", elixir: 8 },
    { id: "balloon", name: "Balloon", type: "Building Targeter", elixir: 5 },
    { id: "goblin-barrel", name: "Goblin Barrel", type: "Spell", elixir: 3 },
    { id: "giant", name: "Giant", type: "Tank", elixir: 5 },
    { id: "pekka", name: "PEKKA", type: "Tank", elixir: 7 },
    { id: "graveyard", name: "Graveyard", type: "Spell", elixir: 5 },
    { id: "ram-rider", name: "Ram Rider", type: "Building Targeter", elixir: 5 },
    { id: "lava-hound", name: "Lava Hound", type: "Flying Tank", elixir: 7 },
    { id: "xbow", name: "X-Bow", type: "Building", elixir: 6 },
    { id: "mortar", name: "Mortar", type: "Building", elixir: 4 },
  ]

  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <header className="bg-blue-900 text-white shadow-md">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <Trophy className="h-8 w-8 text-yellow-400" />
            <h1 className="text-xl md:text-2xl font-bold">Clash Counter Academy</h1>
          </div>
          <nav className="hidden md:flex gap-6">
            <Link href="/" className="hover:text-yellow-400 font-medium">
              Home
            </Link>
            <Link href="/learn" className="hover:text-yellow-400 font-medium">
              Learn
            </Link>
            <Link href="/quiz" className="hover:text-yellow-400 font-medium">
              Quiz
            </Link>
            <Link href="/about" className="hover:text-yellow-400 font-medium">
              About
            </Link>
          </nav>
          <Button variant="outline" className="md:hidden bg-transparent border-white text-white hover:bg-blue-800">
            Menu
          </Button>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow">
        <div className="container mx-auto px-4 py-8">
          <div className="flex items-center gap-2 mb-6">
            <Link href="/" className="text-blue-600 hover:underline">
              Home
            </Link>
            <ChevronRight className="h-4 w-4" />
            <span>Learn</span>
          </div>

          <div className="mb-8">
            <h1 className="text-3xl font-bold mb-4">Win Condition Counters</h1>
            <p className="text-lg text-gray-700 max-w-3xl">
              Select a win condition below to learn about its mechanics, strengths, weaknesses, and the best cards and
              strategies to counter it effectively.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {winConditions.map((condition) => (
              <Card key={condition.id} className="overflow-hidden hover:shadow-lg transition-shadow">
                <div className="h-40 relative bg-gray-200">
                  <Image
                    src={`/placeholder.svg?height=160&width=320&text=${encodeURIComponent(condition.name)}`}
                    alt={condition.name}
                    fill
                    className="object-cover"
                  />
                </div>
                <CardHeader className="pb-2">
                  <CardTitle>{condition.name}</CardTitle>
                  <CardDescription>
                    {condition.type} • {condition.elixir} Elixir
                  </CardDescription>
                </CardHeader>
                <CardContent className="pb-2">
                  <p className="text-sm text-gray-600">
                    Learn how to counter {condition.name} with optimal card placements and timing.
                  </p>
                </CardContent>
                <CardFooter>
                  <Button asChild variant="outline" className="w-full">
                    <Link href={`/learn/${condition.id}`}>
                      <BookOpen className="mr-2 h-4 w-4" />
                      Learn Counters
                    </Link>
                  </Button>
                </CardFooter>
              </Card>
            ))}
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center gap-2 mb-4 md:mb-0">
              <Trophy className="h-6 w-6 text-yellow-400" />
              <span className="text-lg font-bold">Clash Counter Academy</span>
            </div>
            <div className="flex gap-6">
              <Link href="/" className="hover:text-yellow-400">
                Home
              </Link>
              <Link href="/learn" className="hover:text-yellow-400">
                Learn
              </Link>
              <Link href="/quiz" className="hover:text-yellow-400">
                Quiz
              </Link>
              <Link href="/about" className="hover:text-yellow-400">
                About
              </Link>
            </div>
          </div>
          <div className="mt-6 text-center md:text-left text-gray-400 text-sm">
            <p>© {new Date().getFullYear()} Clash Counter Academy. Not affiliated with Supercell.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
